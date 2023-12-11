from django.urls import path
from . import views

urlpatterns = [# Give a name to make dinamyc urls
    path('', views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="posts-detail-page"),
]