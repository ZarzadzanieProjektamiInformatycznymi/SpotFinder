from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Spot, Category
from .forms import SpotForm, SpotSearchForm

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
    return render(request, 'spots/spot_detail.html', {'spot': spot})

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