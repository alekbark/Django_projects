from django.http import Http404
from django.shortcuts import render, redirect
from .models import Person, Child, IceCream, Kiosk, Feedback, Document
from .forms import IceCreamForm, IceCreamFormSet, FeedbackForm, DocumentForm

def universal_list(request, model_name):
    models_map = {
        'persons': Person,
        'children': Child,
        'icecreams': IceCream,
        'kiosks': Kiosk,
    }

    model = models_map.get(model_name)

    if not model:
        raise Http404

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

# HW32
def feedback_create(request):

    if request.method == 'POST':

        form = FeedbackForm(request.POST)

        if form.is_valid():

            Feedback.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )

        return redirect('feedback_success')

    else:
        form = FeedbackForm()

    return render(request, 'feedback_form.html', {'form': form})

def feedback_success(request):

    return render(request, 'feedback_success.html')

# HW37
def upload_document(request):

    if request.method == 'POST':

        form = DocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'document_list'
            )

    else:

        form = DocumentForm()

    return render(
        request,
        'document_form.html',
        {
            'form': form
        }
    )

# HW37
def document_list(request):

    documents = Document.objects.all()

    return render(
        request,
        'document_list.html',
        {'documents': documents}
    )