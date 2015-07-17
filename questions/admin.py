from django.contrib import admin
from .models import Category, Question

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('title','category','date')

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
