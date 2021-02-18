from django.urls import path
from . import views

urlpatterns = [
    # code omitted for brevity
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('action/<int:pk>/', views.UpvoteDetail.as_view()),
    path('action/', views.UpvoteList.as_view()),
]