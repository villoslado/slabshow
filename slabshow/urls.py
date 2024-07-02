from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def redirect_to_feed(request):
    return redirect("feed")


urlpatterns = [
    path("", redirect_to_feed, name="home_page"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("profiles/", include("profiles.urls")),
    path("cards/", include("cards.urls")),
    path("feed/", include("feed.urls")),
    path("followers/", include("followers.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
