from django.conf.urls import url
from django.urls import path
from tcapi import views
from .views import current_user, UserList

urlpatterns = [
    path('current_user/', current_user), # Login
    path('users/', UserList.as_view()), # Registration endpoint
    url(r'^api/users/', views.user_list), # Get all user(s)
    url(r"^api/posts", views.tweet_list), # Get all posts
    url(r"^api/postnew", views.post_tweet_auth_user), # Post new tweet
    url(r"^api/individualposts/(?P<pk>[0-9]+)$", views.tweet_detail),
    url(r"^api/postreactions", views.postreactions_list),
    url(r"^api/postreactions/(?P<pk>[0-9]+)$", views.postreactions_detail),
    url(r"^api/commentreplies", views.commentreplies_list),
    url(r"^api/commentreplies/(?P<pk>[0-9]+)$", views.commentreplies_detail),
]
