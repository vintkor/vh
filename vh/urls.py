from django.contrib import admin
from django.urls import path, include
from vh.settings import MEDIA_URL, MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('shop.urls')),
    path('vh_manager/', include('admin_vh.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
