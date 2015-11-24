"""
Extra context processors for the SkCodeOnlineTester app.
"""

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
            'TITLE': 'Console de test du projet PySkCode',
            'TITLE_SHORT': 'PySkCode Tester',
            'AUTHOR': 'Fabien Batteix',
            'COPYRIGHT': 'TamiaLab 2015',
            'DESCRIPTION': 'Console de test pour le projet PySkCode.',
            'GOOGLE_SITE_VERIFICATION_CODE': '',  # TODO
            'TWITTER_USERNAME': 'skywodd',
        },
        'SITE': {
            'NAME': site.name,
            'DOMAIN': site.domain,
            'PROTO': 'https' if request.is_secure() else 'http'
        }
    }
