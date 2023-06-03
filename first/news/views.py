from django.shortcuts import render, redirect
from .models import Articles
from .forms import Articles_Form


def news_home(request):
    news = Articles.objects.order_by('date')[:2] # order_by - функция, осуществляющая сортировку по заданному параметру(по полям в таблице), в квадратных скобка указывается кол-во записей
    return render(request, 'news/news.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = Articles_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неправильно'

    form = Articles_Form()
    data = { # словарь с полями ввода
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

