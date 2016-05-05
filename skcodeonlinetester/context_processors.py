"""
Extra context processors for the SkCodeOnlineTester app.
"""

from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site


def app_constants(request):
    """
    Constants context processor.
    :param request: the current request.
    :return: All constants for the app.
    """
    site = get_current_site(request)
    return {
        'APP': {
            'TITLE': _('Test console for the PySkCode project'),
            'TITLE_SHORT': _('PySkCode test console'),
            'AUTHOR': 'Fabien Batteix',
            'COPYRIGHT': 'TamiaLab 2016',
            'DESCRIPTION': _('Test console for the PySkCode project.'),
            'GOOGLE_SITE_VERIFICATION_CODE': '',
            'TWITTER_USERNAME': 'skywodd',
            'TWITTER_ACCOUNT_ID': '250273994',
            'FACEBOOK_URL': 'https://www.facebook.com/fabien.batteix',
        },
        'SITE': {
            'NAME': site.name,
            'DOMAIN': site.domain,
            'PROTO': 'https' if request.is_secure() else 'http'
        }
    }
