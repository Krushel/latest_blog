from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from api.models import Post, Comment, Upvote
from django.views.generic import ListView, CreateView, DeleteView

from .forms import AddPostForm
from django.urls import reverse, reverse_lazy


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'articles/register.html'
    success_url = reverse_lazy('front:posts')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('front:posts')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'articles/login.html'


def Logout(request):
    logout(request)
    return redirect('front:login')


class Posts(ListView):
    model = Post
    template_name = 'articles/posts.html'


@login_required(redirect_field_name='front:posts')
def CreateUpvote(request, pk):
    try:
        post = Post.objects.get(id = pk)
    except:
        raise Http404("No such post(")
    postUpvotes = Upvote.objects.filter(post=Post.objects.get(id=pk)).all()
    try:
        postUpvotes.get(owner=request.user)
        postUpvotes.get(owner=request.user).delete()
    except:
        post.upvotes.create(owner=request.user)
    return HttpResponseRedirect( reverse('front:posts',))


class CreatePost(CreateView):
    form_class = AddPostForm
    template_name = 'articles/createpost.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.owner = self.request.user
        post.save()
        return HttpResponseRedirect( reverse('front:posts',))


@login_required(redirect_field_name='front:posts')
def Comments(request, pk):
    if request.method == "POST":
        try:
            post = Post.objects.get(id = pk)
        except:
            raise Http404("No such post(")
        post.comments.create(body = request.POST['comment'], owner=request.user)
        return HttpResponseRedirect( reverse('front:comments', args=(pk,)))
    else:
        try:
            post = Post.objects.get(id = pk)
            comments = post.comments.all()
        except:
            raise Http404("No such post(")
        return render(request, 'articles/comments.html', {"comments": comments, "pk":pk, 'post':post})


@login_required(redirect_field_name='front:posts')
def DeletePost(request, pk):
    try:
        Post.objects.get(id=pk).delete()
    except:
        return Http404
    return HttpResponseRedirect(reverse('front:posts', ))


@login_required(redirect_field_name='front:posts')
def DeleteComment(request, pk):
    try:
        Comment.objects.get(id=pk).delete()
    except:
        return Http404
    return HttpResponseRedirect(reverse('front:posts', ))