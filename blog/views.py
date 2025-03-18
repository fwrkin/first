from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.models import Post


class BlogListView(LoginRequiredMixin,ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(was_publication=True)


class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = (
        "name",
        "description",
        "image",
        "created_at",
        "was_publication",
        "views_counter",
    )
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = (
        "name",
        "description",
        "image",
        "created_at",
        "was_publication",
        "views_counter",
    )
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy("blog:blog_list")
