from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Todo
from django.urls import path
from django.shortcuts import HttpResponseRedirect
from django.utils.html import format_html
admin.site.site_header = 'ToDo Admin Dashboard'


class TodoAdmin(admin.ModelAdmin):
    # exclude = ('completed',)
    fields = ('text', 'font_size')
    list_display = ('text', 'completed', 'font_size_html_display',)
    list_filter = ('completed',)
    change_list_template = 'admin/todo/todo_change_list.html'
    readonly_fields = ('text_preview',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [path('fontsize/<int:size>/', self.change_font_size)]
        return custom_urls + urls

    def change_font_size(self, request, size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, f'Font size changed succesfully to {size}')
        return HttpResponseRedirect('../')

    def font_size_html_display(self, obj):
        display_size = obj.font_size if obj.font_size <=30 else 30
        return format_html(f'<span style="font-size:{obj.font_size}px;">{obj.font_size}</span>')


admin.site.register(Todo, TodoAdmin)
admin.site.unregister(Group)

