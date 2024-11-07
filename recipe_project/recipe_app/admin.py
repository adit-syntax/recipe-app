from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'display_ingredients_preview')
    list_filter = ('created_at',)
    search_fields = ('title', 'ingredients', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 10
    
    fieldsets = (
        ('Recipe Information', {
            'fields': ('title', 'ingredients', 'description')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )

    def display_ingredients_preview(self, obj):
        return obj.ingredients[:50] + '...' if len(obj.ingredients) > 50 else obj.ingredients
    display_ingredients_preview.short_description = 'Ingredients Preview'

    def delete_selected_recipes(self, request, queryset):
        queryset.delete()
    delete_selected_recipes.short_description = "Delete selected recipes"

    actions = [delete_selected_recipes]

    admin.site.site_header = "Recipe Management"
    admin.site.site_title = "Recipe Admin Portal"
    admin.site.index_title = "Welcome to Recipe Admin Portal"