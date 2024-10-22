from django import forms
from main.models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating_value']
        widgets = {
            'rating_value': forms.Select(choices=Rating.RATING)
        }