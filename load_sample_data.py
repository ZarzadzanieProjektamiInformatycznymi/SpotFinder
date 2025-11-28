#LOAD SAMPLE DATA USING python load_sample_data.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SpotFinder.settings")
django.setup()

from django.contrib.auth.models import User
from spots.models import Category, Spot, UserProfile


def run():
    print("Czyszczenie starych danych...")

    Spot.objects.all().delete()
    Category.objects.all().delete()
    UserProfile.objects.all().delete()
    User.objects.filter(username="testuser").delete()

    print("Tworzenie użytkownika testowego...")

    user = User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="test1234"
    )

    UserProfile.objects.create(
        user=user,
        bio="Przykładowy profil testowy.",
        avatar=None
    )

    print("Tworzenie kategorii...")

    cat_park = Category.objects.create(
        name="Park",
        description="Tereny zielone, miejsca do spacerów."
    )

    cat_view = Category.objects.create(
        name="Punkt Widokowy",
        description="Miejsca z pięknym widokiem."
    )

    cat_food = Category.objects.create(
        name="Jedzenie",
        description="Ciekawe lokale gastronomiczne."
    )

    print("Dodawanie przykładowych spotów...")

    Spot.objects.create(
        name="Park Centralny",
        description="Duży park z alejkami i stawem.",
        category=cat_park,
        added_by=user,
        location_lat=52.229675,
        location_lng=21.012230,
    )

    Spot.objects.create(
        name="Wzgórze Widokowe",
        description="Świetny punkt na zachód słońca.",
        category=cat_view,
        added_by=user,
        location_lat=52.237049,
        location_lng=21.017532,
    )

    Spot.objects.create(
        name="Kawiarnia nad Rzeką",
        description="Lokal z dobrą kawą i widokiem na wodę.",
        category=cat_food,
        added_by=user,
        location_lat=52.230841,
        location_lng=21.001029,
    )

    print("Gotowe – dodano przykładowe dane.")


if __name__ == "__main__":
    run()
