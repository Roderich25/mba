from django.contrib import admin
from .models import Choice, Question


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pub_date', 'question_text', 'was_published_recently', 'active']
    list_editable = ['question_text', 'active']
    list_filter = ['active', 'pub_date']
    list_per_page = 50
    date_hierarchy = 'pub_date'
    search_fields = ['question_text__istartswith']
    fieldsets = [
        ('Date of publication', {'fields': ['pub_date']}),
        ('Question', {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInLine]


# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
