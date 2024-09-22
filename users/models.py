from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default='10',
                                      validators=[
                                          MaxValueValidator(99),
                                          MinValueValidator(5)
                                      ])
    gender = models.CharField(max_length=10, choices=GENDER)
    club = models.CharField(max_length=100, default='Клуб не определен')


@receiver(post_save, sender=CustomUser)
def set_club(sender, instance, created, **kwargs):
    if created:
        print('Сигнал обработан. Пользователь создан')

        age = instance.age
        if age < 5:
            instance.club = 'Вы слишком малы'
        elif 5 <= age <= 10:
            instance.club = 'Детский'
        elif 11 <= age <= 17:
            instance.club = 'Подростковый'
        elif 18 <= age <= 45:
            instance.club = 'Взрослый'
        else:
            instance.club = 'Клуб не определен'
        instance.save()

