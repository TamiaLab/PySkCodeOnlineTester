"""
Root URLCONF for the SkCodeOnlineTester project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url


# Root URL patterns configuration
urlpatterns = [

    # Home page
    url(r'^', include('apps.home.urls', namespace='home')),
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
