from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', include("observations.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('jsi18n', JavaScriptCatalog.as_view(), name="js-catalog"),
    path('users/', include("users.urls")),
    path('projects/', include('projects.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
