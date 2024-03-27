from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']