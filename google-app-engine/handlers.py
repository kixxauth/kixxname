"""
  kixxnameWebsite.handlers
  ~~~~~~~~~~~~~~~~~~~~~~~~
  WSGI application request handlers for FWerks (see fwerks.py for more info)
  which use the Werkzeug utilities. All handlers must be subclasses of
  `Handler` from the fwerks `fwerks.py` module. See `fwerks.py` for
  documentation regarding request handlers.

  Werkzeug Response and Request objects are exposed to request handlers and the
  documentation for those Werkzeug classes is at
  http://werkzeug.pocoo.org/documentation/0.6.2/wrappers.html (The source code
  can be found in `werkzeug/wrappers.py`.

  :copyright: (c) 2010 by Kris Walker. All rights reserved.
"""
import os
import time
import logging

import utils
from fwerks import Handler
import dstore
import content

from werkzeug.utils import http_date, cached_property
from werkzeug.exceptions import InternalServerError
from werkzeug.useragents import UserAgent

# Standard 'Do not cache this!' declaration for the cache-control header.
NO_CACHE_HEADER = 'no-cache, no-store, must-revalidate, pre-check=0, post-check=0'

# Determine if we are running locally or not.
ON_DEV_SERVER = os.environ['SERVER_SOFTWARE'].startswith('Development')

def set_common_headers(response):
  """Helper to quickly set some default headers.
  """
  # We don't want IE munging our response, so we set
  # X-XSS-Protection to 0
  response.headers['X-XSS-Protection'] = '0'
  return response

def exception_handler(exception, request, out):
  """To be passed into the fwerks module for general exception handling.

  We define the general exception handling function here for easy access to
  other tools in this module. This function is designed to be passed to the
  FWerks application constructor function in `request.py`.

  `exception` is the exception object that was caught.
  `request` is a Werkzeug request object.
  `out` is a callable used to create a Werkzeug response object.
  """
  logging.exception(exception)
  if ON_DEV_SERVER:
    response = out(utils.trace_out())
    response.status_code = 500
  else:
    # TODO: A nice 500 response.
    response = InternalServerError()
  return response

def not_found(response):
  """To be passed into the fwerks module to handle unmatched paths.

  We define the general 'not found' handler here for easy access to other tools
  in this module. This function is designed to be passed to the FWerks
  application constructor function in `request.py`.

  `response` A pre-constructed response object.
  """
  # TODO: A nice 404 response.
  response = set_common_headers(response)

  # We have to set all the headers using the header dictionary on the response
  # because the NotFound class does not have utility wrappers for them.
  response.headers['Expires'] = '-1'
  response.headers['Pragma'] = 'no-cache'
  response.headers['Cache-Control'] = NO_CACHE_HEADER
  response.headers['Content-Type'] = 'text/html; charset=utf-8'
  response.headers['Connection'] = 'close'
  return response

def request_redirect(response):
  """To be passed into the fwerks module to handle mis-matched paths.

  We define the general 'redirect' handler here for easy access to other tools
  in this module. This function is designed to be passed to the FWerks
  application constructor function in `request.py`.

  `response` A pre-constructed response object.
  """
  # There is no need to format a nice redirect response, since
  # browsers will automatically redirect
  response = set_common_headers(response)

  # Expire in 4 weeks.
  response.headers['Expires'] = http_date(time.time() + (86400 * 28))
  response.headers['Cache-Control'] = 'public, max-age=%d' % (86400 * 28)
  response.headers['Connection'] = 'close'
  return response

class BaseHandler(Handler):

  @cached_property
  def no_persist(self):
    rv = self.request.headers.get('x-request-no-persist', None)
    return (rv and rv == 'true') and True or False

  @cached_property
  def persist_user_agent(self):
    user_agent = UserAgent(self.request.environ)
    if user_agent.browser:
      attrs = (
            user_agent.platform
          , user_agent.browser
          , user_agent.version
          , user_agent.language
          )
      return '%s;%s;%s;%s'% attrs
    return user_agent.string

  def finalize_response(self, response, record_request=True):
    browser_id = self.request.cookies.get('bid')
    browser = None
    request = None
    user_agent = None
    status = response.status_code 
    status_ok = status >= 200 and status < 300 or status is 304

    # Used to avoid datastore writes during automated testing.
    no_persist = self.no_persist

    response = set_common_headers(response)

    # TODO
    #if not browser_id:
      # We also send the browser_id as an ETag in some cases
      #etags = self.request.if_none_match
      #etag = len(etags) and etags.pop() or None
      # If ETag length > 32 (md5) it is a browser key and not a real ETag
      #browser_id = len(etag) > 32 and etag or None
    if not browser_id:
      user_agent = self.persist_user_agent
      browser = dstore.Browser(user_agent=user_agent
                             , init_path=self.request.path
                             , init_referrer=self.request.referrer
                             , init_address=self.request.remote_addr)
      browser.put()
      browser_id = dstore.browser_key(browser)

    # Reset the browser id cookie
    if status_ok:
      response.set_cookie('bid',
                          value=browser_id,
                          expires=(int(time.time()) + 31556926)) # Exp in 1 year.

    if record_request:
      user_agent = user_agent or self.persist_user_agent
      request = dstore.Request(browser=browser_id
                             , user_agent=user_agent
                             , path=self.request.path
                             , referrer=self.request.referrer
                             , address=self.request.remote_addr
                             , status=(response.status_code or 0))
      k = request.put()
      if status_ok:
        response.set_cookie('rid', value=str(k))

    # Delete during automated testing.
    if browser and no_persist:
      browser.delete()
    if request and no_persist:
      request.delete()

    # Caching is private since we're always setting a cookie.
    response.headers['Cache-Control'] = 'private, max-age=%d' % (86400 * 4)

    # Do this last for an accurate conditional response.
    response.add_etag()

    # Only send a response body if the E-Tag does not match.
    return response.make_conditional(self.request)

class VerticalHandler(BaseHandler):
  """Handle requests for 'vertical search' pages."""

  def respond(self):
    # Prepare the response.
    locale, action = self.name.split(',')
    context = content.vertical(locale, action)
    response = set_common_headers(
        self.out(
          utils.render_template('vertical', context)))
    response.mimetype = 'text/html'

    # Expire in 10 days.
    response.expires = int(time.time()) + (86400 * 10)
    return self.finalize_response(response)

  def get(self):
    """Accept the HTTP GET method."""
    return self.respond()

  def head(self):
    """Accept the HTTP HEAD method."""
    return self.respond()

class PriceHandler(BaseHandler):
  """Handle requests for the price schedule page."""

  def respond(self):
    response = set_common_headers(
        self.out(
          utils.render_template('pricing', content.pricing)))
    response.mimetype = 'text/html'

    # Expire in 1 day.
    response.expires = int(time.time()) + 86400
    return self.finalize_response(response)

  def get(self):
    """Accept the HTTP GET method."""
    return self.respond()

  def head(self):
    """Accept the HTTP HEAD method."""
    return self.respond()

class SimpleHandler(BaseHandler):
  """Handle requests for simple named pages."""

  def respond(self):
    response = set_common_headers(
        self.out(
          utils.render_template(self.name, getattr(content, self.name, {}))))
    response.mimetype = 'text/html'

    # Expire in 10 days.
    response.expires = int(time.time()) + (86400 * 10)
    return self.finalize_response(response)

  def get(self):
    """Accept the HTTP GET method."""
    return self.respond()

  def head(self):
    """Accept the HTTP HEAD method."""
    return self.respond()

class StylesheetHandler(Handler):
  """Handle requests for CSS stylesheets."""

  def respond(self):
    name = self.name +'-'+ self.request.args.get('class', 'default')
    response = self.out(utils.render_template(name, type='css'))
    response.mimetype = 'text/css'

    # Expire in 3 days.
    response.expires = int(time.time()) + (86400 *3)

    # Only send a response body if the E-Tag does not match.
    response.add_etag()
    return response.make_conditional(self.request)

  def get(self):
    """Accept the HTTP GET method."""
    return self.respond()

  def head(self):
    """Accept the HTTP HEAD method."""
    return self.respond()


# Create the handler map for export to the request handling script.  As you can
# see, the map is a list of tuples. The first item in each tuple is the URL
# rule for Werkzeug to match. The second item in each tuple is the name of the
# endpoint for Werkzeug. The third item in each tuple is a reference to the
# handler class for the fwerks module to use.
#
# Consult the Werkzeug rule formatting documentation for more info on
# constructing rules:
# http://werkzeug.pocoo.org/documentation/0.6.2/routing.html#rule-format
#
handler_map = [
      ('/poughkeepsie_and_hudson_valley_website_design'
        , 'poughkeepsie_and_hudson_valley,website_design'
        , VerticalHandler)

    , ('/service_and_price_schedule'
        , 'price schedule'
        , PriceHandler)

    , ('/resume', 'resume', SimpleHandler)

    , ('/freelance_programming', 'programming', SimpleHandler)

    , ('/contact', 'contact', SimpleHandler)

    , ('/website_and_mobile_design_portfolio', 'portfolio', SimpleHandler)

    , ('/css/all.css', 'all', StylesheetHandler)
    ]


