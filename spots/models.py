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
    location_lat = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True) # Szerokość geograficzna
    location_lng = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True) # Długość geograficzna
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_spots')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name="ratings")
    value = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'spot')  # jeden użytkownik może ocenić miejsce tylko raz

    def __str__(self):
        return f"{self.user.username} → {self.spot.name}: {self.value}"
    
class Comment(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # zawsze najnowsze jako pierwsze

    def __str__(self):
        return f"Komentarz {self.user.username} → {self.spot.name}"
