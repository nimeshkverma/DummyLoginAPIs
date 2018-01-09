from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^agent/login/$',
        views.Login.as_view(), name='Login'),
    url(r'^agent/(?P<agent_id>[0-9]+)/logout/$',
        views.Logout.as_view(), name='Logout'),
    url(r'^agent/(?P<agent_id>[0-9]+)/noticeboard/$',
        views.NoticeBoard.as_view(), name='NoticeBoard'),
    url(r'^agent/(?P<agent_id>[0-9]+)/customer/$',
        views.CustomerPickup.as_view(), name='CustomerPickup'),
    url(r'^agent/(?P<agent_id>[0-9]+)/customer/(?P<customer_id>[0-9]+)/documents_uploaded/$',
        views.DocumentUploaded.as_view(), name='DocumentUploaded'),
    url(r'^customer/document_type/$',
        views.DocumentType.as_view(), name='DocumentType'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
