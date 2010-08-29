
VERTICAL_DESCRIPTION = ('Kris Walker %s (for fun and profit) right here in %s and %s. '
    'Including %s for iPhone and other mobile phones too.')

PRICING_DESCRIPTION = 'Upfront pricing for your website design, including free.'

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
    , 'hosting'     : 12
    , 'domain_svc' : 7
    , 'seo_svc'    : 12
    }

PRICE_GROWING = 0.15
PRICE_FULL = 0.25

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

def price_level(discount, known):
  return int(known / (1 - discount))

pricing = {
      'page_class': 'pricing'
    , 'description': PRICING_DESCRIPTION
    , 'price_start_domain': BASE_PRICING['domain_reg']
    , 'price_growing_domain': price_level(PRICE_GROWING, BASE_PRICING['domain_reg'])
    , 'price_full_domain': price_level(PRICE_FULL, BASE_PRICING['domain_reg'])
    , 'price_start_seo': BASE_PRICING['seo']
    , 'price_growing_seo': price_level(PRICE_GROWING, BASE_PRICING['seo'])
    , 'price_full_seo': price_level(PRICE_FULL, BASE_PRICING['seo'])
    , 'price_start_hosting_setup': BASE_PRICING['setup']
    , 'price_growing_hosting_setup': price_level(PRICE_GROWING, BASE_PRICING['setup'])
    , 'price_full_hosting_setup': price_level(PRICE_FULL, BASE_PRICING['setup'])
    , 'price_start_package': BASE_PRICING['page'] * 3
    , 'price_growing_package': price_level(PRICE_GROWING, BASE_PRICING['page']) * 3
    , 'price_full_package': price_level(PRICE_FULL, BASE_PRICING['page']) * 3
    , 'price_start_page': BASE_PRICING['page']
    , 'price_growing_page': price_level(PRICE_GROWING, BASE_PRICING['page'])
    , 'price_full_page': price_level(PRICE_FULL, BASE_PRICING['page'])
    , 'price_start_cms': BASE_PRICING['cms']
    , 'price_growing_cms': price_level(PRICE_GROWING, BASE_PRICING['cms'])
    , 'price_full_cms': price_level(PRICE_FULL, BASE_PRICING['cms'])
    , 'price_start_cmspage': BASE_PRICING['cms_page']
    , 'price_growing_cmspage': price_level(PRICE_GROWING, BASE_PRICING['cms_page'])
    , 'price_full_cmspage': price_level(PRICE_FULL, BASE_PRICING['cms_page'])
    , 'price_start_form': BASE_PRICING['form']
    , 'price_growing_form': price_level(PRICE_GROWING, BASE_PRICING['form'])
    , 'price_full_form': price_level(PRICE_FULL, BASE_PRICING['form'])
    , 'price_start_hourly': BASE_PRICING['hourly']
    , 'price_growing_hourly': price_level(PRICE_GROWING, BASE_PRICING['hourly'])
    , 'price_full_hourly': price_level(PRICE_FULL, BASE_PRICING['hourly'])
    , 'price_start_hosting': BASE_PRICING['hosting']
    , 'price_growing_hosting': price_level(PRICE_GROWING, BASE_PRICING['hosting'])
    , 'price_full_hosting': price_level(PRICE_FULL, BASE_PRICING['hosting'])
    , 'price_start_domain_service': BASE_PRICING['domain_svc']
    , 'price_growing_domain_service': price_level(PRICE_GROWING, BASE_PRICING['domain_svc'])
    , 'price_full_domain_service': price_level(PRICE_FULL, BASE_PRICING['domain_svc'])
    , 'price_start_seo_service': BASE_PRICING['seo_svc']
    , 'price_growing_seo_service': price_level(PRICE_GROWING, BASE_PRICING['seo_svc'])
    , 'price_full_seo_service': price_level(PRICE_FULL, BASE_PRICING['seo_svc'])
    }

