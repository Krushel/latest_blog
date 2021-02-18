from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import serializers
from .models import Post, Comment, Upvote
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UpvoteList(generics.ListCreateAPIView):
    queryset = Upvote.objects.all()
    serializer_class = serializers.UpvoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpvoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Upvote.objects.all()
    serializer_class = serializers.UpvoteSerializer
    permission_classes = [IsOwnerOrReadOnly]