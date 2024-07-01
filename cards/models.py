from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    cert_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=4, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    card_number = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    variety = models.CharField(max_length=100, blank=True)
    grade_description = models.CharField(max_length=100, blank=True)
    card_grade = models.CharField(max_length=20, blank=True)
    total_population = models.IntegerField(blank=True, null=True)
    population_higher = models.IntegerField(blank=True, null=True)
    front_image_url = models.URLField(blank=True)
    back_image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
