from django.shortcuts import render
from templating.models import Items


def home_page(request):
    context = {
        'object_list': Items.objects.all()
    }
    return render(request, 'templating/home.html', context)


def contacts_page(request):
    return render(request, 'templating/contacts.html')
