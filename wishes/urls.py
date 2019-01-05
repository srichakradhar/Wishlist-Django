from django.conf.urls import url
from wishes import views

urlpatterns = [
    url(r'^wishes/$',views.wish_list),
    url(r'^wishes/(?P<pk>[0-9]+)/$',views.wish_detail),
]