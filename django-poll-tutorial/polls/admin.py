from django.contrib import admin
from .models import Choice, Question


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date of publication', {'fields': ['pub_date']}),
        ('Question', {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
