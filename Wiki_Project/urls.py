from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/', include('accounts.urls')),
  # path('markdownx/', include('markdownx.urls')), 
  path(r'mdeditor/', include('mdeditor.urls')),
  path('',include('Wiki.urls'))
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
