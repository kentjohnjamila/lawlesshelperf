from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Helper


def home(request):
    context = {
        'posts': Helper.objects.all()
    }
    return render(request, 'helper/home.html', context)

class PostListView(ListView):
    model = Helper
    template_name = 'helper/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Helper


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Helper
    fields = ['helper', 'helper_rank', 'helper_point']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == helper.author:
            return True
        return False

