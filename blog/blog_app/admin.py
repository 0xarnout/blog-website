from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import Article, Tag


admin.site.register(Tag)

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ["headline", "description_tag", "pub_date", "slug"]
    list_display = ["headline", "pub_date", "active", "featured"]
    list_filter = ["active", "featured", "pub_date", "tags__tag"]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'tags':
            kwargs['widget'] = CheckboxSelectMultiple
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    actions = ["mark_active", "mark_inactive", "mark_featured", "mark_not_featured"]

    @admin.action(description="Mark selected articles as active")
    def mark_active(self, request, queryset):
        queryset.update(active=True)
    
    @admin.action(description="Mark selected articles as inactive")
    def mark_inactive(self, request, queryset):
        queryset.update(active=False)
    
    @admin.action(description="Mark selected articles as featured")
    def mark_featured(self, request, queryset):
        queryset.update(featured=True)
    
    @admin.action(description="Mark selected articles as not featured")
    def mark_not_featured(self, request, queryset):
        queryset.update(featured=False)

admin.site.register(Article, ArticleAdmin)