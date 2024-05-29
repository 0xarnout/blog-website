from django.contrib import admin
from .models import Portrait, SiteSettings


class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "last_modified"]
    fieldsets = (
        ('General Config', {
            'fields': ('sitename', 'home_photo', 'home_text', 'placeholder_thumbnail', 'comment_portrait', 'about_photo', 'about_text'),
        }),
        ('SEO', {
            'fields': ('favicon', 'home_description_tag', 'blog_description_tag', 'about_description_tag')
        }),
        ('Contact Details', {
            'fields': ('email', 'github_link', 'discord_link'),
        }),
    )
    def has_delete_permission(self, request, obj=None):
        return False #protect static SiteSettings instance

admin.site.register(SiteSettings, SiteSettingsAdmin)

class PortraitAdmin(admin.ModelAdmin):
    search_fields = ["name", "email_address"]
    list_display = ["__str__", "name", "email_address"]

admin.site.register(Portrait, PortraitAdmin)