from django.shortcuts import render, HttpResponse


def index(request, nom):

    return HttpResponse(f'Bonjour {nom}')

