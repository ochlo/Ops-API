from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ops import views

urlpatterns = [
    url(r'^cmd/$', views.cmds_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.cmds_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
