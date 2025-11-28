from django import forms
from .models import Spot, Category, Rating, Comment 

class SpotForm(forms.ModelForm):
    class Meta:
        model = Spot
        fields = ['name', 'description', 'category', 'location_lat', 'location_lng']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class SpotSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Wyszukaj miejsce")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label="Kategoria")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ten wiersz staje się zbędny, jeśli queryset jest już ustawiony powyżej
        # self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].empty_label = "Wszystkie kategorie"

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']
        widgets = {
            'value': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Napisz komentarz...'
            })
        }
