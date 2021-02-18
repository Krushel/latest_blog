from django import forms
from api.models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ["owner"]

# class AddUpvoteForm(forms.ModelForm):
#     class Meta:
#         model = Upvote
#         field = '__all__'