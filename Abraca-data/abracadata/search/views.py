# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Pet
from django.http import HttpResponse

# Create your views here.


def search_list(request):
    pets = Pet.objects.all().order_by('acquired_date')
    return render(request, 'search/search_list.html', {'pets': pets})


def search_detail(request, slug):
    pet = Pet.objects.get(slug=slug)
    return render(request, 'search/search_detail.html', {'pet': pet})

