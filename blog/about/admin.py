from django.contrib import admin
from .models import Tech, Certification


class TechAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]

admin.site.register(Tech, TechAdmin)

class CertificationAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]

admin.site.register(Certification, CertificationAdmin)