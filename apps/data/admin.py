from django.contrib import admin
from .models import Form, Row, Result


class RowInline(admin.TabularInline):
    model = Row
    extra = 0


class ResultInline(admin.TabularInline):
    model = Result
    extra = 0


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['id', 'datetime']
    inlines = [RowInline, ]


@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    list_display = ['name', 'form_type']
    inlines = [ResultInline, ]
