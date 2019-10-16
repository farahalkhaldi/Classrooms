from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})


class Student(models.Model):
	name = models.CharField(max_length=105)
	date_of_birth = models.DateField()
	ml = 'Male'
	fl = 'Female'
	gender_choices = [
		(ml, 'Male'),
		(fl, 'Female'),
	]
	gender = models.CharField(max_length=6, choices=gender_choices)
	exam_grade = models.IntegerField()
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
