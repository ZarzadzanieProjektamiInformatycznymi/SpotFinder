# LOAD SAMPLE DATA USING python load_sample_data.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SpotFinder.settings")
django.setup()

from django.contrib.auth.models import User
from spots.models import Category, Spot, UserProfile

def run():
    print("--- Rozpoczynanie generowania danych ---")
    print("Czyszczenie starych danych...")

    Spot.objects.all().delete()
    Category.objects.all().delete()
    UserProfile.objects.all().delete()
    
    # Usuwanie wielu użytkowników testowych
    User.objects.filter(username__in=["admin_test", "ania_podrozniczka", "marek_foto", "urban_explorer"]).delete()

    print("Tworzenie użytkowników...")

    users_data = [
        {"username": "admin_test", "email": "admin@example.com", "bio": "Główny administrator systemu."},
        {"username": "ania_podrozniczka", "email": "ania@example.com", "bio": "Uwielbiam odkrywać kawiarnie i parki."},
        {"username": "marek_foto", "email": "marek@example.com", "bio": "Szukam najlepszych kadrów w mieście."},
        {"username": "urban_explorer", "email": "urban@example.com", "bio": "Interesują mnie zapomniane zabytki i architektura."}
    ]

    created_users = []
    for u_info in users_data:
        u = User.objects.create_user(username=u_info['username'], email=u_info['email'], password="test1234")
        UserProfile.objects.create(user=u, bio=u_info['bio'])
        created_users.append(u)

    print("Tworzenie kategorii...")

    categories = {
        "Park": Category.objects.create(name="Park", description="Tereny zielone, miejsca do spacerów."),
        "Widok": Category.objects.create(name="Punkt Widokowy", description="Miejsca z pięknym widokiem na panoramę miasta."),
        "Jedzenie": Category.objects.create(name="Jedzenie", description="Ciekawe lokale gastronomiczne, kawiarnie i restauracje."),
        "Kultura": Category.objects.create(name="Kultura i Sztuka", description="Muzea, galerie i instalacje artystyczne."),
        "Zabytki": Category.objects.create(name="Zabytki", description="Historyczne budowle i ważne miejsca pamięci."),
        "Natura": Category.objects.create(name="Natura", description="Dzika przyroda w granicach miasta, lasy i rezerwaty.")
    }

    print("Dodawanie przykładowych spotów...")

    spots_data = [
        # --- Kategorie: Park / Natura ---
        {
            "name": "Łazienki Królewskie",
            "description": "Najpiękniejszy kompleks ogrodowy w Warszawie z Pawilonem na Wodzie.",
            "cat": categories["Park"], "user": created_users[1], "lat": 52.2144, "lng": 21.0345
        },
        {
            "name": "Rezerwat przyrody Las Kabacki",
            "description": "Ogromny teren leśny na południu miasta, idealny na rower.",
            "cat": categories["Natura"], "user": created_users[3], "lat": 52.1333, "lng": 21.0333
        },
        # --- Kategorie: Punkty Widokowe ---
        {
            "name": "Taras Widokowy PKiN",
            "description": "Widok z 30. piętra na całą stolicę. Obowiązkowy punkt dla turystów.",
            "cat": categories["Widok"], "user": created_users[0], "lat": 52.2318, "lng": 21.0060
        },
        {
            "name": "Góra Gnojna",
            "description": "Punkt widokowy na Starym Mieście z widokiem na Wisłę i Pragę.",
            "cat": categories["Widok"], "user": created_users[2], "lat": 52.2497, "lng": 21.0133
        },
        # --- Kategorie: Jedzenie ---
        {
            "name": "Hala Koszyki",
            "description": "Odrestaurowana hala targowa z mnóstwem restauracji z całego świata.",
            "cat": categories["Jedzenie"], "user": created_users[1], "lat": 52.2221, "lng": 21.0116
        },
        {
            "name": "Kawiarnia w bibliotece BUW",
            "description": "Spokojne miejsce na kawę połączone z wizytą w ogrodach na dachu.",
            "cat": categories["Jedzenie"], "user": created_users[2], "lat": 52.2425, "lng": 21.0245
        },
        # --- Kategorie: Kultura / Zabytki ---
        {
            "name": "Muzeum Narodowe",
            "description": "Gmach pełen skarbów sztuki polskiej i światowej.",
            "cat": categories["Kultura"], "user": created_users[0], "lat": 52.2316, "lng": 21.0249
        },
        {
            "name": "Neon Muzeum",
            "description": "Unikalne muzeum poświęcone warszawskim neonom z czasów PRL.",
            "cat": categories["Kultura"], "user": created_users[3], "lat": 52.2483, "lng": 21.0592
        },
        {
            "name": "Zamek Królewski",
            "description": "Symbol odbudowanej Warszawy, serce Starego Miasta.",
            "cat": categories["Zabytki"], "user": created_users[0], "lat": 52.2479, "lng": 21.0145
        },
    ]

    for spot in spots_data:
        Spot.objects.create(
            name=spot["name"],
            description=spot["description"],
            category=spot["cat"],
            added_by=spot["user"],
            location_lat=spot["lat"],
            location_lng=spot["lng"]
        )

    print(f"Gotowe! Utworzono:")
    print(f"- {User.objects.count()} użytkowników")
    print(f"- {Category.objects.count()} kategorii")
    print(f"- {Spot.objects.count()} interesujących miejsc")

if __name__ == "__main__":
    run()