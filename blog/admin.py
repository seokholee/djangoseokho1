from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']

admin.site.register(Category, CategoryAdmin)
