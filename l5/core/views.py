from django.shortcuts import render, redirect
from .models import Person, Child, IceCream, Kiosk
from .forms import IceCreamForm, IceCreamFormSet

def universal_list(request, model_name):
    models_map = {
        'persons': Person,
        'children': Child,
        'icecreams': IceCream,
        'kiosks': Kiosk,
    }

    model = models_map.get(model_name)

    if not model:
        return render(request, '404.html')  # можно упростить позже

    objects = model.objects.all()

    return render(request, 'list.html', {
        'objects': objects,
        'model_name': model_name
    })

def create_icecream(request):

    if request.method == 'POST':
        form = IceCreamForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = IceCreamForm()

    return render(request, 'icecream_form.html', {
        'form': form
    })

def create_icecreams(request):

    if request.method == 'POST':
        formset = IceCreamFormSet(request.POST)

        if formset.is_valid():
            formset.save()
            return redirect('/icecreams/')
        else:
            print(formset.errors)

    else:
        formset = IceCreamFormSet()

    return render(
        request,
        'icecream_formset.html',
        {'formset': formset}
    )