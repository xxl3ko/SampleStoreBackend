from django.shortcuts import render

from store.models import Sample


# Create your views here.

def main_page(request):
    return render(request, 'index.html', {'samples': Sample.objects.all})
