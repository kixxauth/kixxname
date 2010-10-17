import decimal
import urllib
import time

VERTICAL_DESCRIPTION = ('Kris Walker %s (for fun and profit) right here in %s and %s. '
    'Including %s for iPhone and other mobile phones too.')
PRICING_DESCRIPTION = 'Upfront pricing for your website design... Including free options.'
RESUME_DESCRIPTION = "Kris Walker's web development, computer programming, and life long resume."
CONTACT_DESCRIPTION = "Kris Walker's contact information. (In hcard microformat.)"
PORTFOLIO_DESCRIPTION = "Kris Walker's design portfolio for the web... Including mobile websites."
PROGRAMMING_DESCRIPTION = "Kris Walker does computer programming to bend computers to your will."

# All thumb images should be 450 x 300
PORTFOLIO = [
      {
        'title': 'Jill McKellan'
      , 'description': """This website has been built for a talented freelance writer. The chosen style was old European, but without being too dark. The site is a customized WordPress installation for full blogging support. It also features page interactions driven by cutting edge JavaScript technology. Not only to the page interactions jump to life when you click on them, but they are also live feeds from Jill's Facebook and Twitter accounts."""
      , 'source': '/img/portfolio-jill_mckellan-thumb.png'
      , 'alt': 'Screenshot Jill McKellan website.'
      , 'href': 'http://www.jillmckellan.com/'
      }
    , {
        'title': 'The Fireworks Project'
      , 'description': """This website is the first for this start up software company. It is a custom design that includes analytical data tracking to measure the site traffic and how long visitors stay to read any particular page, as well as the links they click on within the site. All this data is important to the site owners for tracking the success of their marketing efforts."""
      , 'source': '/img/portfolio-the_fireworks_project-thumb.png'
      , 'alt': 'Screenshot of The Fireworks Project website.'
      , 'href': 'http://www.fireworksproject.com/'
      }
    , {
        'title': 'Crown Construction'
      , 'description': """This project is not a website, but a custom web application built for internal use by a home remodeling firm. It allows them to keep all their customer records organized and available nomatter where they are. The design is a custom design just for this purpose."""
      , 'source': '/img/portfolio-crown_construction-thumb.png'
      , 'alt': 'Screenshot of the Crown Construction web application.'
      , 'href': '/img/big-screenshot-crown-construction.png'
      }
    , {
        'title': 'Lisa Walker Photography'
      , 'description': """A nice photographer's website, including a slide show for her portfolio. This website is designed with a content management system so the website owner can update her portfolio of photographs without needing any special web technology skills. The goal of any photography website, of course, is to show off the photographs, and that is what this website was designed to do."""
      , 'source': '/img/portfolio-lisa_walker_photography-thumb.png'
      , 'alt': 'Screenshot of Lisa Walker Photography website.'
      , 'href': 'http://www.lisawalkerphotography.com/'
      }
    ]

LOCALES = {
      'poughkeepsie_and_hudson_valley': ['The Hudson Valley', 'Poughkeepsie']
    }

ACTIONS = {

      # Targeting 'website design'
      'website_design': [
          'website design' # Page title, description * for iPhone and ...
        , 'website designer &amp; builder' # Page intro (header)
        , 'designs and builds websites' # description * right here in ...
        , 'websites' # Portfolio link.
        , 'Creating websites' # First content section.
        , ''
        ]

      # Targeting 'web and website design'
    , 'mixed': [
          'web design' # Page title, description * for iPhone and ...
        , 'web designer and developer' # Page intro (header)
        , 'designs and builds websites' # description * right here in ...
        , 'websites' # Portfolio link.
        , 'Creating websites' # First content section.
        , ''
        ]
    }

BASE_PRICING = {
      'domain_reg'  : 107
    , 'seo'         : 247
    , 'setup'       : 227
    , 'page'        : 247
    , 'cms'         : 397
    , 'cms_page'    : 297
    , 'form'        : 797
    , 'hourly'      : 57
    , 'hosting'     : 9
    , 'domain_svc'  : 7
    , 'seo_svc'     : 11
    }

DISCOUNT_GROWING = decimal.Decimal(str(0.15))
DISCOUNT_BOOTSTRAP = decimal.Decimal(str(0.25))

RESUME_EXPERIENCES = [
      {
        'title': 'Bootstrapper'
      , 'org_url': 'http://www.fireworksproject.com/'
      , 'org': 'The Fireworks Project'
      , 'location': 'Virtually Everywhere'
      , 'start_mf': '2009-04-01'
      , 'start_read': 'April 2009'
      , 'end_mf': time.strftime('%Y-%m-%d')
      , 'end_read': 'present'
      , 'description': """Since April of 2009 I have been bootrapping a unique kind of software firm. Our aim is to change the way software is built and used by small businesses. While we're at it, we're also exploring a new way to structure a corporation. Stop by and check us out at <a title="The Fireworks Project builds small business software." href="http://www.fireworksproject.com">www.fireworksproject.com</a>"""
      }
    , {
        'title': 'Freelancer'
      , 'org_url': 'http://www.kixx.name/'
      , 'org': 'Fireworks Computer Systems'
      , 'location': 'Poughkeepsie, NY'
      , 'start_mf': '2008-01-01'
      , 'start_read': 'January 2008'
      , 'end_mf': time.strftime('%Y-%m-%d')
      , 'end_read': 'present'
      , 'description': """I design and build websites as well as handle a multitude of programming tasks.  For more information about web design and development you should check out my home page at <a title="Kris Walker's web design home page." href="http://www.kixx.name/"> www.kixx.name</a>. To get the scoop on my programming abilities check out my programming page at <a title="Kris Walker does computer programming and software engineering." href="http://www.kixx.name/freelance_programming">www.kixx.name/freelance_programming</a>.  Or, you can check out the tag list of skills at the bottom of this page."""
      }
    , {
        'title': 'Regional Manager'
      , 'org_url': 'http://www.gentlegiantmoving.com/'
      , 'org': 'Gentle Giant Moving Company'
      , 'location': 'New York City'
      , 'start_mf': '2005-05-01'
      , 'start_read': 'May 2005'
      , 'end_mf': '2008-01-01'
      , 'end_read': 'January 2008'
      , 'description': """I bootstrapped the regional branch location in New York City for Gentle Giant. The personal growth and development I experienced while working on this project has been invaluable to me. I learned to grasp opportunity, execute on ideas, manage people, keep happy customers, and provide opportunity for everyone under my management. Most of all I learned how important it is to maintain a good quality of life for everyone involved in an entrepreneurial project, even for my self.""" }
    , {
        'title': 'High School Rowing Coach'
      , 'org_url': 'http://www.greenwichwaterclub.com/'
      , 'org': 'Greenwich Water Club'
      , 'location': 'Cos Cob, CT'
      , 'start_mf': '2004-08-01'
      , 'start_read': 'August 2004'
      , 'end_mf': '2005-05-01'
      , 'end_read': 'May 2005'
      , 'description': """Coaching is one of the most rewarding things I've ever done. Someday I'm going to "retire" and just be a coach.""" }
    , {
        'title': 'Runner &amp; Cyclist'
      , 'org_url': 'http://www.kixx.name/'
      , 'org': 'Just for me.'
      , 'location': 'Anywhere'
      , 'start_mf': '2002-03-01'
      , 'start_read': 'March 2002'
      , 'end_mf': time.strftime('%Y-%m-%d')
      , 'end_read': 'present'
      , 'description': """I ran the Boston Marathon twice, but twice is enough. I did it in 3:35 and 3:45.  I&#39;ve also ridden the 150 mile road ride from Boston to Vermont.  I would really like to do that again someday."""
      }
    , {
        'title': 'Mover'
      , 'org_url': 'http://www.gentlegiantmoving.com/'
      , 'org': 'Gentle Giant Moving Company'
      , 'location': 'Boston, MA'
      , 'start_mf': '2001-09-01'
      , 'start_read': 'September 2001'
      , 'end_mf': '2004-08-01'
      , 'end_read': 'August 2004'
      , 'description': """My best guess is that I have moved a little over 2,000 customers for Gentle Giant (I would never do that job for any other organization). I met and interacted with a more diverse collection of individuals than most people will ever get the chance to. The company attracts the best and most interesting customers in the industry and employs amazing people.""" }
    , {
        'title': 'Fork Truck Operator'
      , 'org_url': 'http://www.bestwaylumber.com/'
      , 'org': 'Bestway Enterprises, Inc.'
      , 'location': 'Cortland, NY'
      , 'start_mf': '1999-05-01'
      , 'start_read': 'May 1999'
      , 'end_mf': '2000-09-01'
      , 'end_read': 'September 2000'
      , 'description': """Used fork trucks to unload rail cars, sort stacks of lumber, and feed lumber into treatment or kiln drying. Bestway produced 600,000 board feet of treated lumber per day with a skeleton crew. This is where I learned that efficiency pays big dividends.""" }
    ]

RESUME_TAGS = [
      'programming'
    , 'web design'
    , 'web development'
    , 'front end'
    , 'back end'
    , 'Firefox extensions'
    , 'HTML'
    , 'CSS'
    , 'JavaScript'
    , 'Python'
    , 'PHP'
    , 'Perl'
    , 'Erlang'
    , 'jQuery'
    , 'Dojo'
    , 'YUI'
    , 'Node.js'
    , 'Google App Engine'
    , 'Amazon Web Services'
    , 'WSGI'
    , 'Pylons'
    , 'Django'
    , 'Werkzeug'
    , 'Drupal'
    , 'Wordpress'
    , 'NoSQL'
    , 'CouchDB'
    , 'MongoDB'
    , 'MySQL'
    , 'XPCOM'
    , 'Apache'
    , 'HTTP'
    , 'OAuth'
    , 'OpenID'
    , 'Extreme Programming'
    , 'Agile Development'
    , 'Scrum'
    ]

def vertical(locale, action):
  rv = {}
  locale = LOCALES[locale]
  actions = ACTIONS[action]
  rv['page_class'] = 'vertical'
  rv['super_location'] = locale[0]
  rv['sub_location'] = locale[1]
  rv['title_actions'] = actions[0].capitalize()
  rv['skills'] = actions[1]
  rv['description'] = (VERTICAL_DESCRIPTION % (
                                               actions[2]
                                             , locale[1]
                                             , locale[0]
                                             , actions[0]))
  rv['home_page'] = actions[2]
  rv['portfolio'] = actions[3]
  rv['actions'] = actions[4]
  rv['item'] = actions[0]
  return rv

def full_price_level(known):
  return int(known / (1 - DISCOUNT_BOOTSTRAP))

def growing_price_level(known):
  full = known / (1 - DISCOUNT_BOOTSTRAP)
  return int(full * (1 - DISCOUNT_GROWING))

pricing = {
      'page_class': 'pricing'
    , 'description': PRICING_DESCRIPTION
    , 'price_start_domain': BASE_PRICING['domain_reg']
    , 'price_growing_domain': growing_price_level(BASE_PRICING['domain_reg'])
    , 'price_full_domain': full_price_level(BASE_PRICING['domain_reg'])
    , 'price_start_seo': BASE_PRICING['seo']
    , 'price_growing_seo': growing_price_level(BASE_PRICING['seo'])
    , 'price_full_seo': full_price_level(BASE_PRICING['seo'])
    , 'price_start_hosting_setup': BASE_PRICING['setup']
    , 'price_growing_hosting_setup': growing_price_level(BASE_PRICING['setup'])
    , 'price_full_hosting_setup': full_price_level(BASE_PRICING['setup'])
    , 'price_start_package': BASE_PRICING['page'] * 2
    , 'price_growing_package': growing_price_level((BASE_PRICING['page'] * 2))
    , 'price_full_package': full_price_level((BASE_PRICING['page'] * 2))
    , 'price_start_page': BASE_PRICING['page']
    , 'price_growing_page': growing_price_level(BASE_PRICING['page'])
    , 'price_full_page': full_price_level(BASE_PRICING['page'])
    , 'price_start_cms': BASE_PRICING['cms']
    , 'price_growing_cms': growing_price_level(BASE_PRICING['cms'])
    , 'price_full_cms': full_price_level(BASE_PRICING['cms'])
    , 'price_start_cmspage': BASE_PRICING['cms_page']
    , 'price_growing_cmspage': growing_price_level(BASE_PRICING['cms_page'])
    , 'price_full_cmspage': full_price_level(BASE_PRICING['cms_page'])
    , 'price_start_form': BASE_PRICING['form']
    , 'price_growing_form': growing_price_level(BASE_PRICING['form'])
    , 'price_full_form': full_price_level(BASE_PRICING['form'])
    , 'price_start_hourly': BASE_PRICING['hourly']
    , 'price_growing_hourly': growing_price_level(BASE_PRICING['hourly'])
    , 'price_full_hourly': full_price_level(BASE_PRICING['hourly'])
    , 'price_start_hosting': BASE_PRICING['hosting'] * 12
    , 'price_growing_hosting': growing_price_level((BASE_PRICING['hosting'] * 12))
    , 'price_full_hosting': full_price_level((BASE_PRICING['hosting'] * 12))
    , 'price_start_domain_service': BASE_PRICING['domain_svc'] * 12
    , 'price_growing_domain_service': growing_price_level((BASE_PRICING['domain_svc'] * 12))
    , 'price_full_domain_service': full_price_level((BASE_PRICING['domain_svc'] * 12))
    , 'price_start_seo_service': BASE_PRICING['seo_svc'] * 12
    , 'price_growing_seo_service': growing_price_level((BASE_PRICING['seo_svc'] * 12))
    , 'price_full_seo_service': full_price_level((BASE_PRICING['seo_svc'] * 12))
    }

# Start Up package
pricing['price_starter_package_bootstrap'] = (pricing['price_start_hosting'] +
                                              pricing['price_start_domain_service'])

pricing['price_starter_package_growing'] = (pricing['price_growing_hosting'] +
                                            pricing['price_growing_domain_service'])

pricing['price_starter_package_full'] = (pricing['price_full_hosting'] +
                                         pricing['price_full_domain_service'])

# Customer Magnet package
pricing['price_seo_package_bootstrap'] = (pricing['price_starter_package_bootstrap'] +
                                          pricing['price_start_seo_service'])

pricing['price_seo_package_growing'] = (pricing['price_starter_package_growing'] +
                                        pricing['price_growing_seo_service'])

pricing['price_seo_package_full'] = (pricing['price_starter_package_full'] +
                                     pricing['price_full_seo_service'])


# Time Saver package
pricing['price_cms_package_setup_bootstrap'] = (pricing['price_start_cmspage'] * 2) + pricing['price_start_cms']
pricing['price_cms_package_setup_growing'] = (pricing['price_growing_cmspage'] * 2) + pricing['price_growing_cms']
pricing['price_cms_package_setup_full'] = (pricing['price_full_cmspage'] * 2) + pricing['price_full_cms']

# Custom Design package
pricing['price_custom_package_setup_bootstrap'] = (pricing['price_start_package'] + pricing['price_cms_package_setup_bootstrap'])
pricing['price_custom_package_setup_growing'] = (pricing['price_growing_package'] + pricing['price_cms_package_setup_growing'])
pricing['price_custom_package_setup_full'] = (pricing['price_full_package'] + pricing['price_cms_package_setup_full'])

def resume_tag(tag):
  return {'url':'http://www.technorati.com/tag/'+ urllib.quote(tag), 'name': tag}

resume = {
      'page_class': 'resume'
    , 'description': RESUME_DESCRIPTION
    , 'resume_experiences': RESUME_EXPERIENCES
    , 'resume_tags': map(resume_tag, RESUME_TAGS)
    }

contact = {
    'page_class': 'contact'
    , 'description': CONTACT_DESCRIPTION
    }

portfolio = {
      'page_class': 'portfolio'
    , 'description': PORTFOLIO_DESCRIPTION
    , 'portfolio': PORTFOLIO
    }

programming = {
      'page_class': 'programming'
    , 'description': PROGRAMMING_DESCRIPTION
    , 'resume_tags': map(resume_tag, RESUME_TAGS)
    }

