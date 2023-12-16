from django import forms
from.models import File
from.models import Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FileForm(forms.ModelForm):
    class Meta:
        model=File
        fields='__all__'
