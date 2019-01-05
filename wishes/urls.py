from django.conf.urls import url
from wishes import views

urlpatterns = [
    # url(r'^wishes/$',views.wish_list),
    # url(r'^wishes/(?P<pk>[0-9]+)/$',views.wish_detail),
    url(r'^wishes/$',views.WishList.as_view()),
    url(r'^wishes/(?P<pk>[0-9]+)/$',views.WishDetail.as_view()),
]