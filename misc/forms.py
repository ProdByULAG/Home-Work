from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from misc.models import Category


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=4, label="Введите имя категории",
                           widget=TextInput())

    def clean_name(self):
        category = Category.objects.filter(name=self.cleaned_data['name'])

        if len(category) != 0:
            raise ValidationError("Такакя категория уже есть!")
        else:
            return self.cleaned_data['name']