from django.shortcuts import render


def index(request):  # Здесь мы описываем, что мы будем показывать пользователю
    data = {
        'title': 'Главная страница!!',
        'values': ['Misha', 'Ivan', 'Hello']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
