from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['posts'] = 3
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
