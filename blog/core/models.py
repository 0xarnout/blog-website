from django.db import models


class Portrait(models.Model):
    name = models.CharField(max_length=25, unique=True)
    email_address = models.EmailField()
    portrait_photo = models.ImageField(upload_to="core/portraits")
    def __str__(self):
        return f"Portrait photo of: {self.name}."

class SiteSettings(models.Model):
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    id = models.PositiveSmallIntegerField(primary_key=True, default=1, editable=False)
    last_modified = models.DateTimeField(auto_now=True)
    sitename = models.CharField(max_length=30)
    home_photo = models.ImageField(upload_to="core/sitesettings/home_photo")
    home_text = models.TextField()
    placeholder_thumbnail = models.ImageField(upload_to="core/sitesettings/placeholder_thumbnail", verbose_name="Placeholder article thumbnail")
    comment_portrait = models.ImageField(upload_to="core/sitesettings/comment_portrait")
    about_photo = models.ImageField(upload_to="core/sitesettings/about_photo")
    about_text = models.TextField()
    favicon = models.ImageField(upload_to="core/sitesettings/favicon", blank=True) 
    home_description_tag = models.TextField()
    blog_description_tag = models.TextField()
    about_description_tag = models.TextField()
    email = models.EmailField()
    github_link = models.URLField(blank=True)
    discord_link = models.URLField(blank=True)
    def __str__(self):
        return "Site Settings"
    def get():
        return SiteSettings.objects.get(pk=1)