from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    

class PostCreateView(CreateView):
    model = Post
    fields = ['body']
    def get_success_url(self):
        return reverse('blog:detail', 
                       args=[self.object.pk])