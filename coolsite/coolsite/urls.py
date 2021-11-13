from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from coolsite import settings
from women.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("women.urls")),
    path("captcha/", include("captcha.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
