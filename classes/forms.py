from django import forms
from django.contrib.auth.models import User

from .models import Classroom, Student

class ClassroomForm(forms.ModelForm):
	class Meta:
		model = Classroom
		exclude = ['teacher']

class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']

		widgets = {
			"password": forms.PasswordInput()
		}


class SigninForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ['classroom']