from django.contrib import admin

# Register your models here.
from .models import *

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

admin.site.register(buku)
admin.site.register(anggota)