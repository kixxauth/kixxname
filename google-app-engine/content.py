import decimal

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
    , 'hosting'     : 9
    , 'domain_svc'  : 7
    , 'seo_svc'     : 11
    }

DISCOUNT_GROWING = decimal.Decimal(str(0.15))
DISCOUNT_BOOTSTRAP = decimal.Decimal(str(0.25))

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


# Custom Design package
pricing['price_custom_package_setup_bootstrap'] = pricing['price_start_package']
pricing['price_custom_package_setup_growing'] = pricing['price_growing_package']
pricing['price_custom_package_setup_full'] = pricing['price_full_package']

# Time Saver package
pricing['price_cms_package_setup_bootstrap'] = (pricing['price_start_cmspage'] * 2) + pricing['price_start_cms']
pricing['price_cms_package_setup_growing'] = (pricing['price_growing_cmspage'] * 2) + pricing['price_growing_cms']
pricing['price_cms_package_setup_full'] = (pricing['price_full_cmspage'] * 2) + pricing['price_full_cms']

