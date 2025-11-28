from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Spot, Category, Rating
from .forms import SpotForm, SpotSearchForm, RatingForm

def spot_list(request):
    form = SpotSearchForm(request.GET)
    spots = Spot.objects.all().order_by('-created_at')

    if form.is_valid():
        query = form.cleaned_data.get('query')
        category = form.cleaned_data.get('category')

        if query:
            spots = spots.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if category:
            spots = spots.filter(category=category)

    context = {
        'spots': spots,
        'form': form,
    }
    return render(request, 'spots/spot_list.html', context)

def spot_detail(request, pk):
    spot = get_object_or_404(Spot, pk=pk)

    ratings = spot.ratings.all()
    if ratings.exists():
        avg_rating = sum(r.value for r in ratings) / ratings.count()
    else:
        avg_rating = None

    return render(request, 'spots/spot_detail.html', {
        'spot': spot,
        'avg_rating': avg_rating,
    })

@login_required
def spot_create(request):
    if request.method == 'POST':
        form = SpotForm(request.POST)
        if form.is_valid():
            spot = form.save(commit=False)
            spot.added_by = request.user
            spot.save()
            return redirect('spot_detail', pk=spot.pk)
    else:
        form = SpotForm()
    return render(request, 'spots/spot_form.html', {'form': form, 'title': 'Dodaj nowe miejsce'})

@login_required
def spot_update(request, pk):
    spot = get_object_or_404(Spot, pk=pk)
    # Tylko właściciel może edytować
    if request.user != spot.added_by:
        return redirect('spot_detail', pk=spot.pk) # Można dodać komunikat o braku uprawnień

    if request.method == 'POST':
        form = SpotForm(request.POST, instance=spot)
        if form.is_valid():
            form.save()
            return redirect('spot_detail', pk=spot.pk)
    else:
        form = SpotForm(instance=spot)
    return render(request, 'spots/spot_form.html', {'form': form, 'title': 'Edytuj miejsce'})

@login_required
def spot_delete(request, pk):
    spot = get_object_or_404(Spot, pk=pk)
    # Tylko właściciel może usunąć
    if request.user != spot.added_by:
        return redirect('spot_detail', pk=spot.pk)

    if request.method == 'POST':
        spot.delete()
        return redirect('spot_list')
    return render(request, 'spots/spot_confirm_delete.html', {'spot': spot})

@login_required
def rate_spot(request, spot_id):
    spot = get_object_or_404(Spot, id=spot_id)

    try:
        rating = Rating.objects.get(user=request.user, spot=spot)
    except Rating.DoesNotExist:
        rating = None

    if request.method == "POST":
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.user = request.user
            new_rating.spot = spot
            new_rating.save()
            return redirect("spot_detail", pk=spot.id)
    else:
        form = RatingForm(instance=rating)

    return render(request, "spots/rate_spot.html", {"spot": spot, "form": form})