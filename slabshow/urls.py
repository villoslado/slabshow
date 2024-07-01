from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("profiles/", include("profiles.urls")),
    path("cards/", include("cards.urls")),
    path("feed/", include("feed.urls")),
    path("followers/", include("followers.urls")),
]
