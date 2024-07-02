from django.shortcuts import render, get_object_or_404
from .models import Card


def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    return render(request, "cards/card_detail.html", {"card": card})
