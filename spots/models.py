from django.db import models
from django.contrib.auth.models import User # Użyjemy wbudowanego Usera na początek

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True, verbose_name="O mnie")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Profil użytkownika {self.user.username}"


class Spot(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='spots')
    image = models.ImageField(upload_to='spots_images/', blank=True, null=True, verbose_name="Zdjęcie")
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True) # Szerokość geograficzna
    location_lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True) # Długość geograficzna
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_spots')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name