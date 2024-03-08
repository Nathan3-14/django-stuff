from django import forms
from django.db import models

# Create your models here.

class NameForm(forms.Form):
    name = forms.CharField(label="Name: ", max_length=50)
