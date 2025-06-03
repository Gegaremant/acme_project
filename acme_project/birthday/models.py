from django.db import models
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse
# Импортируется функция-валидатор.
from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязаетльное поле', max_length=20
        )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', blank=True, upload_to='birthday_images')

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    # получить абсолютный URL объекта
    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})
