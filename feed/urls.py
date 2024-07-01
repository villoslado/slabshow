from django.urls import path
from . import views

urlpatterns = [
    path("", views.feed_view, name="feed"),
]
