from django.urls import path
from . import views

urlpatterns = [
    path(
        "<str:username>/",
        views.profile_view,
        name="profile",
    ),
    path(
        "<str:username>/upload/",
        views.upload_cert_number,
        name="upload_cert_number",
    ),
]
