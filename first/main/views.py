from django.shortcuts import render


def index(request):  # Здесь мы описываем, что мы будем показывать пользователю
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
