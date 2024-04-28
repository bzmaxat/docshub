from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'})
    )


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя'})
    )
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите фамилию'})
    )
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'})
    )
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'})
    )
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'})
    )

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
