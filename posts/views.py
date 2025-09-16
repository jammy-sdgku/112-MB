from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    model = Post
    context_object_name = 'post_list'
    paginate_by = 10