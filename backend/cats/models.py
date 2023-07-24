from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Achievement(models.Model):
    name = models.CharField(max_length=64, verbose_name='Наименование')

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=16, verbose_name='Имя')
    color = models.CharField(max_length=16, verbose_name='Цвет')
    birth_year = models.IntegerField(verbose_name='Дата рождения')
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE,
	verbose_name='Владелец'
        )
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat',
		verbose_name='Достижение')
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None,
	verbose_name='Фото'
        )

    def __str__(self):
        return self.name


class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.cat}'