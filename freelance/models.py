from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save

from django.contrib.auth.models import User

# ---Test models---.

# --- Заказы ----# --- Заказы ----# --- Заказы ----# --- Заказы ----# --- Заказы ----
class Task(models.Model):
    title        = models.CharField(max_length=255 , verbose_name = 'Заголовок')
    slug         = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content      = models.TextField(blank=True, verbose_name = 'Описание заказа')
    photo        = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name = 'Баннер заказа')
    time_create  = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата Создания')
    time_update  = models.DateTimeField(auto_now=True, verbose_name = 'Дата обновления')
    is_published = models.BooleanField(default=True)
    price        = models.CharField(max_length=20, verbose_name = 'Стоимость заказа')
    main_cat     = models.ForeignKey('Main_Category', on_delete=models.PROTECT, null = True, verbose_name = 'Главная категория')
    cat          = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name = 'Категория')
    user         = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['time_create', 'title']


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Task, self).save(*args, **kwargs)

  # --- Заказы ----# --- Заказы ----# --- Заказы ----# --- Заказы ----  # --- Заказы ----

# ---Подрубрики---
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name = 'Баннер категории')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
# ---Подрубрики---

# ---Рубрики---
class Main_Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Главная категория")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name = 'Баннер главных категорий')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Главная категория'
        verbose_name_plural = 'Главные категории'
        ordering = ['id']
# ---Рубрики---


#----Профиль пользователя----
class Profile(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    name         = models.CharField(max_length=30,null=True, blank=True)
    surname      = models.CharField(max_length=50,null=True, blank=True)
    facebook     = models.CharField(max_length=50, null=True, blank=True)
    twitter      = models.CharField(max_length=50, null=True, blank=True)
    instagram    = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    about        = models.TextField(null=True, blank=True)
    raiting      = models.IntegerField(max_length=100,null=True, blank=True)
    launguage    = models.CharField(max_length=100,null=True, blank=True)
    experience   = models.CharField(max_length=100,null=True, blank=True)
    avatar       = models.ImageField(upload_to="photos/%Y/%m/%d/")

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ['name', 'surname']

    def __str__(self):
        """Return username."""
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_name': self.name})
#/----Профиль пользователя----/

#/----Коментарии----/
class Comment(models.Model):
    """Comment model."""

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Task, on_delete=models.PROTECT)
    comment = models.TextField(max_length=5000)
    

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Коментарий пользователя'
        verbose_name_plural = 'Коментарии пользователей'
        ordering = ['user', 'post']
#/----Коментарии----/
