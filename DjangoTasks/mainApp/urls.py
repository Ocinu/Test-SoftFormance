from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('my_posts', views.my_posts, name='my_posts'),
    path('tracking_posts', views.tracking_posts, name='tracking_posts'),
    path('following', views.following, name='following'),
]
