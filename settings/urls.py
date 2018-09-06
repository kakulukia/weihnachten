from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from flea_market.views import EventsViewSet, InquiryViewSet
from sample_app.views import index

router = DefaultRouter()
router.register(r'events', EventsViewSet)
router.register(r'inquiries', InquiryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^api/', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
