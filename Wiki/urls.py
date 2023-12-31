from django.urls import path, re_path
from .views import index, detail, create, update, delete, page_settings

app_name = "Wiki"

urlpatterns = [
  path('',index, name='index'),
  path('create/',create, name='create'),
  re_path(r'^create/(?P<slug>.+)/$', create, name='create_with_slug'),
  path('settings/',page_settings, name='page_settings'),
  re_path(r'^detail/(?P<username>[^/]+)/(?P<slug>.+)/$', detail, name='detail'),
  re_path(r'^update/(?P<username>[^/]+)/(?P<slug>.+)/$', update, name='update'),
  path('delete/<int:id>/', delete, name='delete'),
]
