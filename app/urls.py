from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', index),
    url(r'p/(?P<slug>[^/]+)/single/(?P<comment_id>\d+)', comments_view, name='comments_view'),
    url(r'p/(?P<slug>[^/]+)/page/(?P<page>\d+)', comments_view, name='comments_view'),
    url(r'p/(?P<slug>[^/]+)', comments_view, name='comments_view'),

]
