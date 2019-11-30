# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from slugify import slugify
from django.shortcuts import render
from .models import Pet
from bs4 import BeautifulSoup
import requests


pet_ids = set()


def search_list(request):
    savepets()
    pets = Pet.objects.all().order_by('acquired_date')
    return render(request, 'search/search_list.html', {'pets': pets})


def get_month(month):
    switcher = {
        "January": '1',
        "February": '2',
        "March": '3',
        "April": '4',
        "May": '5',
        "June": '6',
        "July": '7',
        "August": '8',
        "September": '9',
        "October": '10',
        "November": '11',
        "December": '12'
    }
    return switcher.get(month, '1')


def savepets():
    source = requests.get('https://www.talgov.com/animals/kennel-dogs.aspx').text
    soup = BeautifulSoup(source, 'lxml')
    pets = soup.find('table', class_='table_data')

    for pet_data in pets.tbody.find_all('td', valign='top'):
        pet_description = str(pet_data).split('<br/>')[1]
        parsebycommas = pet_description.split(',')
        parsebyspace = parsebycommas[0].split(' ')
        sex_description = parsebyspace[len(parsebyspace) - 1]
        spayed_description = parsebyspace[len(parsebyspace) - 2]
        breed = parsebycommas[1].split('.')[0][1:]
        color = parsebycommas[1].split('generally ')[1].split(' in')[0]
        pet_name_text = pet_data.strong.text.split('-')[0]
        petid_text = pet_data.strong.text.split('-')[1]
        pet_name = pet_name_text[0:len(pet_name_text)]
        petid = petid_text[1:len(petid_text)+1]
        pet_image_link = 'http://www.petharbor.com:80/get_image.asp?RES=thumb&ID=' + str(petid) + '&LOCATION=TLLS'
        years = int(parsebycommas[2].split(' ')[8])

        if parsebycommas[2].split(' ')[11].isnumeric():
            months = int(parsebycommas[2].split(' ')[11])
        else:
            months = 0

        age = years*12 + months

        if sex_description == 'female':
            sex = 1
        elif sex_description == 'male':
            sex = 0
        else:
            sex = -1

        if spayed_description is not 'unaltered':
            spayed = True
        elif spayed_description == 'spayed' or spayed_description == 'neutered':
            spayed = False
        else:
            spayed = None

        wordset = set()
        for stri in pet_description.split(' '):
            wordset.add(stri)

        if 'foster' in wordset:
            fostered = True
        else:
            fostered = False

        date_list = parsebycommas[2].split(' ')
        day = date_list[len(date_list) - 1]
        month = date_list[len(date_list) - 2]

        month_num = get_month(month)

        year = parsebycommas[3].split('.')[0][1:]
        acquired_date = year + '-' + month_num + '-' + day

        if petid != 'No ID':
            if petid not in pet_ids:
                pet_object = Pet()
                pet_object.name = pet_name
                pet_object.age = age
                pet_object.sex = sex
                pet_object.spayed = spayed
                pet_object.color = color
                pet_object.fostered = fostered
                pet_object.description = pet_description
                pet_object.acquired_date = acquired_date
                pet_object.pet_id = petid
                pet_object.slug = slugify(pet_object.name)
                pet_object.image = pet_image_link
                pet_object.breed = breed
                pet_ids.add(petid)
                pet_object.save()
        else:
            pet_object = Pet()
            pet_object.name = pet_name
            pet_object.age = age
            pet_object.sex = sex
            pet_object.spayed = spayed
            pet_object.color = color
            pet_object.fostered = fostered
            pet_object.description = pet_description
            pet_object.pet_id = petid
            pet_object.breed = breed
            pet_object.slug = slugify(pet_object.name)
            pet_object.image = pet_image_link
            pet_ids.add(petid)
            pet_object.save()


def search_detail(request, slug):
    pet = Pet.objects.get(slug=slug)
    return render(request, 'search/search_detail.html', {'pet': pet})


