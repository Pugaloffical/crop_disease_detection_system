from django.contrib import admin
from .models import Category, Disease, UploadedImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name', 'keywords']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ['original_filename', 'user', 'category', 'predicted_disease', 'prediction_text', 'uploaded_at']
    list_filter = ['category', 'predicted_disease', 'uploaded_at']
    search_fields = ['original_filename', 'prediction_text']
