import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from profiles.models import Profile
from profiles.keys import PSA_API_KEY
from cards.models import Card

BASE_API_URL = "https://api.psacard.com/publicapi/cert/GetByCertNumber"
IMAGE_API_URL = "https://api.psacard.com/publicapi/cert/GetImagesByCertNumber"


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)

    search_query = request.GET.get("search", "")
    if search_query:
        cards = Card.objects.filter(
            Q(user=user)
            & (
                Q(title__icontains=search_query)
                | Q(brand__icontains=search_query)
                | Q(subject__icontains=search_query)
                | Q(category__icontains=search_query)
                | Q(year__icontains=search_query)
            )
        )
    else:
        cards = Card.objects.filter(user=user)

    return render(
        request,
        "profiles/profile.html",
        {
            "profile_user": user,
            "cards": cards,
            "search_query": search_query,
        },
    )


@login_required
def upload_cert_number(request, username):
    if request.method == "POST":
        cert_number = request.POST["cert_number"]
        user = get_object_or_404(User, username=username)

        url = f"{BASE_API_URL}/{cert_number}"
        headers = {
            "Authorization": f"bearer {PSA_API_KEY}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json().get("PSACert", {})

            image_url = f"{IMAGE_API_URL}/{cert_number}"
            image_response = requests.get(image_url, headers=headers)
            image_response.raise_for_status()

            images_data = image_response.json()

            front_image_url = ""
            back_image_url = ""
            for image in images_data:
                if image.get("IsFrontImage"):
                    front_image_url = image.get("ImageURL", "")
                else:
                    back_image_url = image.get("ImageURL", "")

            card = Card(
                user=user,
                cert_number=cert_number,
                title=data.get("Subject", ""),
                year=data.get("Year", ""),
                brand=data.get("Brand", ""),
                category=data.get("Category", ""),
                card_number=data.get("CardNumber", ""),
                subject=data.get("Subject", ""),
                variety=data.get("Variety", ""),
                grade_description=data.get("GradeDescription", ""),
                card_grade=data.get("CardGrade", ""),
                total_population=data.get("TotalPopulation", 0),
                population_higher=data.get("PopulationHigher", 0),
                front_image_url=front_image_url,
                back_image_url=back_image_url,
            )
            card.save()

            messages.success(
                request,
                f"Card with certification number {cert_number} has been successfully added.",
            )
            return redirect("profile", username=username)

        except requests.RequestException as e:
            messages.error(
                request,
                f"An error occurred while fetching card data: {str(e)}",
            )
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")

    return render(request, "profiles/upload_cert_number.html")


def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    return render(request, "cards/card_detail.html", {"card": card})
