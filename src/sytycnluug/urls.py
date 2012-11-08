from django.conf.urls import patterns, url


from sytycnluug.ratezzz.views import TalkView

urlpatterns = patterns('',
    url(r'^ratezzz/$', TalkView.as_view()),
    url(r'^ratezzz/(?P<pk>\d+)/$', TalkView.as_view()),
)
