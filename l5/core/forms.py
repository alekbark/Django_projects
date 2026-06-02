from django import forms
from .models import IceCream

# форма для создания записи с мороженым HW25
class IceCreamForm(forms.ModelForm):

    class Meta:
        model = IceCream
        fields = ('name', 'kind', 'price')