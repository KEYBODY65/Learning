from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class Articles_Form(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date'] # Поля ввода
        widgets = { # Преукрашивания
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Дата публикации'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            })
        }
