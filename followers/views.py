from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Follower
from django.contrib.auth.decorators import login_required


@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    Follower.objects.get_or_create(
        user=request.user,
        followed_user=user_to_follow,
    )
    return redirect("profile", username=username)


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    Follower.objects.filter(
        user=request.user,
        followed_user=user_to_unfollow,
    ).delete()
    return redirect("profile", username=username)
