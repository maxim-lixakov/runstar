from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings

urlpatterns = [
                  path(r'admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path(r'', include('main.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

