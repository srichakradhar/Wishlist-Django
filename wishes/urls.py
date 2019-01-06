from django.conf.urls import url, include
from wishes import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^$', views.api_root),
]

# urlpatterns = [
#     # url(r'^wishes/$', views.wish_list),
#     # url(r'^wishes/(?P<pk>[0-9]+)/$', views.wish_detail),
#     url(r'^wishes/$',views.WishList.as_view(), name='wish-list'),
#     url(r'^wishes/(?P<pk>[0-9]+)/$',views.WishDetail.as_view(), name='wish-detail'),
# ]

# urlpatterns += [
#     url(r'^users/$',views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(), name='user-detail'),
# ]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

router = DefaultRouter()
router.register(r'wishes', views.WishViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns += router.urls