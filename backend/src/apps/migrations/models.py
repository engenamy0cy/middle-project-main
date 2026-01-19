from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #кастомная модель пользователя
    #username - уже создано в абстрактнм пользователе
    #password - уже создано в абстрактнм пользователе
    #добавим опционные поля
    #спец поле для почты EmailField
    email = models.EmailField(unique=True)
    #поле для большого кол-ва текста(str)
    description = models.TextField()
    #поле для символа опр колличества с ограничением максимум 255
    phone = models.CharField(max_length=11,unique=True,blank=True,null=True)
    #2 вида поле для картинок
    avatar = models.ImageField(upload_to='avatars/')
    #Если вы зраните не у себя в сервере картинки
    #храните их на удаленке или дайте пользователю загрузить аватар по ссылке
    image = models.URLField()

    #добавляем флажок auth группы людей
    #и также задаем related name для изображения конфлитов
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user',
        blank=True
    )

    def __str__(self):
        return self.username