from django.conf.urls import url, include
from wishes import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url(r'^wishes/$',views.wish_list),
    # url(r'^wishes/(?P<pk>[0-9]+)/$',views.wish_detail),
    url(r'^wishes/$',views.WishList.as_view()),
    url(r'^wishes/(?P<pk>[0-9]+)/$',views.WishDetail.as_view()),
]

urlpatterns += [
    url(r'^users/$',views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)