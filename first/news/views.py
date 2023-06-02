from django.shortcuts import render
from .models import Articles


def news_home(request):
    news = Articles.objects.order_by('date')[:1] # order_by - функция, осуществляющая сортировку по заданному параметру(по полям в таблице), в квадратных скобка указывается кол-во записей
    return render(request, 'news/news.html', {'news': news})
