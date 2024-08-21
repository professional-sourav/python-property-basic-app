from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
import logging

from .models import Property

from .forms import UploadFileForm

# Create your views here.
def index(request):

    properties = Property.objects.order_by('-id')

    return render(request, 'property/index.html', {
        'properties': properties
    })

def add_new(request: HttpRequest):

    if request.method == 'POST':
        new_property = Property.objects.create(
            title=request.POST['property_title'],
            description=request.POST['property_description'],
            type=request.POST['property_type'],
            age=request.POST['property_age'],
        )

        new_property.save()

        form = UploadFileForm(request.POST, request.FILES)

        print(form.is_valid())

        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.property_id = new_property.pk
            attachment.save()

        return HttpResponseRedirect(reverse('index'))

    form = UploadFileForm()

    return render(
        request,
        'property/add_new.html',
        {'result': 'ok', 'form': form}
    )


def list_view(request: HttpRequest):
    properties = Property.objects

    query = request.GET

    if query:

        # Single filtering

        # if 'age' in query:
        #     age = query['age']
        #     properties = properties.filter(age=age)
        #
        # if 'type' in query:
        #     property_type = query['type']
        #     properties = properties.filter(type__iexact=property_type)

        # Multiple filtering
        properties = properties.filter(
            age=query['age'] if 'age' in query else None,
            type__iexact=query['type'] if 'type' in query else None,
        )

    properties = properties.order_by('-id')

    return render(
        request,
        'property/list.html',
        {
            'properties': properties,
            'ages': range(1, 60),
            'query': query
        }
    )

