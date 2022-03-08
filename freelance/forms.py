from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import *

#----Форма по созданию заказов----
class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['main_cat'].empty_label = "Рубрика не выбрана"
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Task
        fields = ['user',
                  'title',
                  'slug',
                  'content',
                  'photo',
                  'is_published',
                  'cat',
                  'main_cat',
                  'price']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input-url'}),
            'content': forms.Textarea(attrs={'class': 'craft_nazvanie-info'}),
            'price': forms.TextInput(attrs={'class': 'form-input-price'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')

        return title

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if len(slug) > 50:
            raise ValidationError('Длина превышает 50 символов')

        return slug
#----Форма по созданию заказов----
#----Форма по созданию заказов----

#----Обновление профиля#----
class UpdateTaskForm(forms.ModelForm):
    
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].empty_label = "Ты в курсе что здесь пусто?"
        self.fields['content'].empty_label = "Ты в курсе что здесь пусто?"

     class Meta:
        model = Task
        fields = [
                  'title',
                  'content',
                  'photo',
                  'price']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'craft_nazvanie-info'}),
            'price': forms.TextInput(attrs={'class': 'form-input-price'}),
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 50:
                raise ValidationError('Длина превышает 50 символов')

            return title

#----Обновление профиля#----#----Обновление профиля#----

#---- Форма Регистрации---
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

#---- Форма Регистрации---

#---- Форма Авторизации---
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

#---- Форма Авторизации---


#----Обновление профиля#----
class UpdateProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = "Укажите ваше имя"
        self.fields['about'].empty_label = "Расскажите о себе"

    class Meta:
        model = Profile
        fields = ['user',
                  'name',
                  'surname',
                  'avatar',
                  'experience',
                  'launguage',
                  'about',
                  'phone_number',
                  'instagram',
                  'twitter',
                  'facebook']
        exclude = ['user']

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
            'about': forms.Textarea(attrs={'class': 'craft_nazvanie-info'}),
            'launguage': forms.TextInput(attrs={'class': 'form-input-price'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 50:
            raise ValidationError('Длина превышает 50 символов')

        return name

    def clean_surename(self):
        surename = self.cleaned_data['surname']
        if len(surename) > 50:
            raise ValidationError('Длина превышает 50 символов')

        return surename

#----Обновление профиля#----
#----Обновление профиля#----

#--- Обновление данных о пользователе
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
#--- Обновление данных о пользователе
#--- Обновление данных о пользователе

def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg

class CommentOnPost(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'craft_nazvanie-info'}),
        }

    def clean_title(self):
        title = self.cleaned_data['comment']
        if len(title) > 500:
            raise ValidationError('Длина превышает 500 символов')

        return title
