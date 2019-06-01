from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib import messages

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog
from .forms import BlogForm
from .consts import ConstMessage

class BlogListView(ListView):
    queryset = Blog.objects.all().order_by('-posted_date')
    context_object_name = "blogs"
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"

class BlogCreateView(LoginRequiredMixin ,CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("index")
    template_name = "blog/blog_create_form.html"

    login_url = "/login"

    def form_valid(self, form):
        messages.success(self.request, ConstMessage.SAVE_SUCCESS)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, ConstMessage.SAVE_ERROR)
        return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin ,UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_update_form.html"

    login_url = "/login"

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk": blog_pk})
        return url

    def form_valid(self, form):
        messages.success(self.request, ConstMessage.UPDATE_SUCCESS)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, ConstMessage.UPDATE_EROOR)
        return super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin ,DeleteView):
    model = Blog
    success_url = reverse_lazy("index")

    login_url = "/login"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, ConstMessage.DELETE_SUCCESS)
        return super().delete(request, *args, **kwargs)