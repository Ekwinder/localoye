from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Categories"

class Question(models.Model):
	title = models.CharField(max_length=300)
	category = models.ForeignKey('Category')
	date = models.DateTimeField(default=timezone.now)
	answer = models.CharField(max_length=600,default='default')

	def __unicode__(self):
		return self.title