
from django.urls import path
from .views import *

urlpatterns = [
    path('' , home , name="home"),
    path('login/' , login_view , name="login_view"),
    path('register/' , register_view , name="register_view"),
    path('add-blog/' , add_blog, name="add_blog"),
    path('about_me/' , about_me, name="about_me"),
    path('user_list/' , user_list, name="user_list"),
    path('blog-detail/<slug>' , blog_detail , name="blog_detail"),
    path('see-blog/' , see_blog , name="see_blog"),
    path('blog/' , blog , name="blog"),
    path('blog-delete/<id>' , blog_delete , name="blog_delete"),
    path('blog-update/<slug>/' , blog_update , name="blog_update"),
    path('logout-view/' , logout_view , name="logout_view"),
    path('verify/<token>/' , verify , name="verify")
]
