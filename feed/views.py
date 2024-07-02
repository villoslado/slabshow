from django.shortcuts import render
from cards.models import Card
from django.contrib.auth.decorators import login_required


@login_required
def feed_view(request):
    following_users = request.user.following.all().values_list(
        "followed_user", flat=True
    )
    cards = Card.objects.filter(user__in=following_users).order_by("?")[:1]
    return render(request, "feed/feed.html", {"cards": cards})
