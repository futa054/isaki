from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib import messages

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog
from .forms import BlogForm, SearchForm
from .consts import ConstMessage

from django.db.models import Q

from datetime import datetime, timedelta, date

class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    paginate_by = 5

    def post(self, request, *args, **kwargs):
        form_value = [
            self.request.POST.get('fromDate', None),
            self.request.POST.get('toDate', None),
            self.request.POST.get('postedBy', None),
        ]
        request.session['form_value'] = form_value
        # ページネーションエラーを防ぐ
        self.request.GET = self.request.GET.copy()
        self.request.GET.clear()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sessionにセット
        fromDate = None
        toDate = None
        postedBy = None
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            fromDate = form_value[0]
            toDate = form_value[1]
            postedBy = form_value[2]
        default_data = {'fromDate': fromDate,  # from日付
                        'toDate': toDate,  # to日付
                        'postedBy': postedBy,
                        }
        search_form = SearchForm(initial=default_data) # 検索フォーム
        context['search_form'] = search_form
        return context

    def get_queryset(self):
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            fromDate = form_value[0]
            toDateStr = form_value[1]
            postedBy = form_value[2]
            # 検索条件
            condition_fromDate = Q()
            condition_toDate = Q()    
            condition_postedBy = Q()          
            if fromDate != "":
                condition_fromDate = Q(posted_date__gte=fromDate)
            if toDateStr != "":
                date_format = "%Y-%m-%d"
                toDateTime = datetime.strptime(toDateStr, date_format)
                toDateTime += timedelta(days=1)
                toDate = toDateTime.strftime(date_format)
                condition_toDate = Q(posted_date__lt=toDate)
            if postedBy != "":
                condition_postedBy = Q(author=postedBy)
            queryset = Blog.objects.select_related().filter(condition_fromDate & condition_toDate & condition_postedBy)
        else:
            queryset = Blog.objects.all()
        
        return queryset.order_by('-posted_date')

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
        form.instance.author_id = self.request.user.id
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