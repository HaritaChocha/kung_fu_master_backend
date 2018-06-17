from django import forms
from django.contrib.auth.models import User

from .models import Student, Guardian

class StudentForm(forms.ModelForm):

    class Meta:
        ['first_name', 'last_name', 'address', 'city', 'date_of_birth', 'date_of_joining', 'phone_number', 'rank',
         'guardian']


class GuardianForm(forms.ModelForm):

    class Meta:
        model = Guardian
        fields = ['first_name', 'last_name', 'address', 'city', 'phone_number', 'relation']
