from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post, Comments
from .forms import CreatePostForm


class IndexView(ListView):
    model = Post
    paginate_by = 2
    context_object_name = 'posts'
    template_name = 'index.html'


class PostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('index')
