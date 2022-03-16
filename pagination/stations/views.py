import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        CONTENT = []
        for row in reader:
            CONTENT.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    bus_stations = CONTENT[(page_number- 1) * 10:page_number  * 10]

    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
