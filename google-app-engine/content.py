
VERTICAL_DESCRIPTION = ('Kris Walker %s right here in %s and %s. '
    'Including %s for iPhone and other mobile phones. (for fun and profit)')

INTRO = 'I %s'

CONTENT_FIRST = "It's amazing how much a good %s can do."

LOCALES = {
      'poughkeepsie_and_hudson_valley': ['The Hudson Valley', 'Poughkeepsie']
    }

ACTIONS = {

      # Targeting 'website design'
      'website_design': [
          'website design' # Page title, description * for iPhone and ...
        , 'website designer and builder' # Page intro (header)
        , 'designs and builds websites' # description * right here in ...
        , 'websites' # Portfolio link.
        , 'Creating usable websites' # First content section.
        , ''
        ]
    }

def vertical(locale, action):
  rv = {}
  locale = LOCALES[locale]
  actions = ACTIONS[action]
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
  rv['content_first'] = CONTENT_FIRST % actions[0]
  return rv

