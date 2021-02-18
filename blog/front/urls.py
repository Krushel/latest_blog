from django.urls import path
from . import views
from .views import Posts, CreatePost, RegisterUser, LoginUser

app_name = 'front'


urlpatterns = [
    path('signup', RegisterUser.as_view(), name = 'register'),
    path('login', LoginUser.as_view(), name = 'login'),
    path('logout', views.Logout, name = 'logout'),
    path('', Posts.as_view(), name = 'posts'),
    path('<int:pk>', views.Comments, name = 'comments'),
    path('create', CreatePost.as_view(), name='create'),
    path('<int:pk>/upvote', views.CreateUpvote, name = 'upvote'),
    path('<int:pk>/delete', views.DeletePost, name = 'deletePost'),
    path('<int:pk>/commentDelete', views.DeleteComment, name = 'deleteComment'),
]