from django.contrib import admin

# Register your models here.
from django.contrib import admin
# ---------------------------------- [edit] ---------------------------------- #
from .models import Question
from .models import Answer


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
# ---------------------------------------------------------------------------- #
