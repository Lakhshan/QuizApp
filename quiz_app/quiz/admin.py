from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, UserQuizSession

admin.site.register(Question)
admin.site.register(UserQuizSession)
