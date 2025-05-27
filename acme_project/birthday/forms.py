# birthday/forms.py
from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(max_length=20)  # Максимальная длина
    last_name = forms.CharField(required=False)  # Не обязательное поле
    birthday = forms.DateField()
