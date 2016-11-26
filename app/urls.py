from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', index),

    # Note: order is important. No time to write a better regex. Go, go, go!
    url(r'p/(?P<slug>[^/]+)/c/(?P<comment_id>\d+)', comments_view, name='comments_view_single'),
    url(r'p/(?P<slug>[^/]+)/c/add'                , comments_view, name='comments_add'),
    url(r'p/(?P<slug>[^/]+)/(?P<page>\d+)'        , comments_view, name='comments_view_page'),
    url(r'p/(?P<slug>[^/]+)'                      , comments_view, name='comments_view'),

]
