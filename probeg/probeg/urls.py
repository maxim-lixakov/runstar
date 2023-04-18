from django.contrib import admin
from django.urls import include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'cms/', include(wagtailadmin_urls)),
    path(r'documents/', include(wagtaildocs_urls)),
    path(r'runstar/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)