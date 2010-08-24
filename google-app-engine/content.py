
VERTICAL_DESCRIPTION = ('Kris Walker %s (for fun and profit) right here in %s and %s. '
    'Including %s for iPhone and other mobile phones too.')

PRICING_DESCRIPTION = 'Upfront pricing for your website design, including free.'

INTRO = 'I %s'

LOCALES = {
      'poughkeepsie_and_hudson_valley': ['The Hudson Valley', 'Poughkeepsie']
    }

ACTIONS = {

      # Targeting 'website design'
      'website_design': [
          'website design' # Page title, description * for iPhone and ...
        , 'website designer & builder' # Page intro (header)
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

pricing = {
      'page_class': 'pricing'
    , 'description': PRICING_DESCRIPTION
    }

