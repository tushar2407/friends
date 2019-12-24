from django.urls import path
from django.conf.urls import url
from . import views 
urlpatterns=[
    url(r'^home/$',views.Post.as_view(),name='post'),
    url(r'^profile/(?P<pk>\d+)/$',views.Users.as_view(),name='profile'),
    #url(r'^profile/(?P<username>[\w.@+-]+)/$',views.Users.as_view(),name='profile'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',views.change_friend,name='change_friend'),
] 
'''
    above middle part is to give both add and lose friend 
    .+ means anything further 
    '''