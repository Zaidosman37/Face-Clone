from django.urls import path
from . import views
urlpatterns = [
        path('',views.index,name='index'),
        path('home',views.home,name='home'),
        path('profile',views.profile,name='profile'),
        path('logout',views.signout,name='logout'),
        path('register',views.register,name = 'register'),
        path('update',views.update,name = 'update'),
        path('post',views.create_post,name='post')
              ]