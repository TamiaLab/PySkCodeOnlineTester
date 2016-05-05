"""
Root URLCONF for the SkCodeOnlineTester project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps import views as sitemaps_views


# Patch admin site
admin.site.site_title = 'TamiaLab administration'
admin.site.site_header = 'TamiaLab administration'


# Root URL patterns configuration
urlpatterns = [

    # Home page
    url(r'^', include('apps.home.urls', namespace='home')),

    # Admin pages
    url(r'^admin/', include(admin.site.urls)),
]

# Sitemap index and section
sitemaps = {
    # TODO Add all sitemaps here
}
urlpatterns += [
    url(r'^sitemap\.xml$', sitemaps_views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemaps_views.sitemap, {'sitemaps': sitemaps}),
]

# Static/media files serving for debug ONLY, static() do nothing when DEBUG=False
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
