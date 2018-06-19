from django import forms
from django.contrib.auth.models import User

from .models import Student, Guardian, Enrollment

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'address', 'city', 'date_of_birth', 'date_of_joining', 'phone_number', 'rank',]


class GuardianForm(forms.ModelForm):

    class Meta:
        model = Guardian
        fields = ['first_name', 'last_name', 'address', 'city', 'phone_number', 'relation']

class EnrollmentForm(forms.ModelForm):

    class Meta:
        model = Enrollment
        fields = ['batch']