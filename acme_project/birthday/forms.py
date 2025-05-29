# birthday/forms.py
from django import forms


class BirthdayForm(forms.Form):
    # Максимальная длина
    first_name = forms.CharField(max_length=20, label='Имя')
    # Не обязательное поле
    last_name = forms.CharField(required=False, label='Фамилия',
                                help_text='Необязательное поле')
    birthday = forms.DateField(
        label='Дата рождения',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date'})
        )
