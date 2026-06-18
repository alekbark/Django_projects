from django import forms
from .models import IceCream, Document
from captcha.fields import CaptchaField

# форма для создания записи с мороженым HW25
class IceCreamForm(forms.ModelForm):

    class Meta:
        model = IceCream
        fields = ('name', 'kind', 'recommended_price')

IceCreamFormSet = forms.modelformset_factory(
    IceCream,
    form=IceCreamForm,
    extra=3
)

# HW32
class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

# HW37
class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document

        fields = [
            'title',
            'file',
        ]

