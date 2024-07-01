from django.urls import path
from . import views

urlpatterns = [
    path("<int:card_id>/", views.card_detail, name="card_detail"),
]
