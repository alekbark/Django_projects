from django.forms import ModelForm, modelformset_factory
from .models import IceCream

# форма для создания записи с мороженым HW25
class IceCreamForm(ModelForm):

    class Meta:
        model = IceCream
        fields = ('name', 'kind', 'price')

IceCreamFormSet = modelformset_factory(
    IceCream,
    form=IceCreamForm,
    extra=3
)