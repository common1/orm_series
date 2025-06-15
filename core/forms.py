from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import Restaurant

# class RatingForm(forms.Form):
#     rating = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'restaurant_type')