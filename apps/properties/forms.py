from django import forms

from .models import Property, Unit


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'description', 'cr_number', 'manager', 'image']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['property', 'unit_type', 'rent_price', 'is_furnished', 'before_images']