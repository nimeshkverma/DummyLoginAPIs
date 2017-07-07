from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^customer/login/$', views.Config.as_view(), name='config'),
    url(r'^customer/data_log/$', views.DataLogList.as_view()),
    url(r'^customer/data_log/(?P<pk>[0-9]+)/$', views.DataLogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
