from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comments
from .forms import CreatePostForm


class IndexView(ListView):
    paginate_by = 2
    context_object_name = 'posts'
    template_name = 'index.html'
    queryset = Post.objects.all().order_by('date_posted')


class PostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(post=self.object)
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('index')
