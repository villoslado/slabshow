from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Card


def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    return render(request, "cards/card_detail.html", {"card": card})


@login_required
def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id, user=request.user)
    if request.method == "POST":
        card.delete()
        messages.success(request, "Card has been deleted successfully.")
        return redirect("profile", username=request.user.username)
    return render(request, "cards/confirm_delete.html", {"card": card})
