from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='helper-home'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
]
