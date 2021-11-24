from django.db import models
from django.views.generic import DeleteView, ListView
from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
