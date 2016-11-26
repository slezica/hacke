from django.conf.urls import url

from .views import *


urlpatterns = [
    # Note: order is important. No time to write a better regex. Go, go, go!
    url(r'^$', index),

    url(r'action/add_reaction', add_reaction, name='add_reaction'),
    url(r'action/attach_comment', attach_comment, name='attach_comment'),

    url(r'p/(?P<slug>[^/]+)/c/(?P<comment_id>\d+)', poster_view , name='poster_view_comment'),
    url(r'p/(?P<slug>[^/]+)/(?P<page>\d+)'        , poster_view , name='poster_view_page'),
    url(r'p/(?P<slug>[^/]+)'                      , poster_view , name='poster_view'),

]
