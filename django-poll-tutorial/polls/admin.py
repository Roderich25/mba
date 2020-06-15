from django.contrib import admin
from .models import Choice, Question
from django.utils import timezone


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 2


def created_now(modeladmin, requets, queryset):
    queryset.update(pub_date=timezone.now())


created_now.short_description = 'Mark as published now'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    actions = [created_now]
    list_display = ['pub_date', 'question_text', 'was_published_recently', 'active']
    list_editable = ['question_text', 'active']
    list_filter = ['active', 'pub_date']
    list_per_page = 50
    date_hierarchy = 'pub_date'
    search_fields = ['question_text__istartswith']
    fieldsets = [
        ('None', {'fields': ['active']}),
        ('Date of publication', {'classes': ('collapse',), 'fields': ['pub_date']}),
        ('Question', {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInLine]
    save_on_top = True
    # radio_fields = {'active': admin.VERTICAL}


# admin.site.register(Question, QuestionAdmin)
