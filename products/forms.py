from django.forms import ModelForm
from .models import Rating
from django.utils.html import strip_tags

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

    def clean_product_id(self):
        product_id = self.cleaned_data["product_id"]
        return strip_tags(product_id)

    def clean_rating_value(self):
        rating_value = self.cleaned_data["rating_value"]
        return strip_tags(rating_value)