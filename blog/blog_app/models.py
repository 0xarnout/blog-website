from django_ckeditor_5 import fields
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from random import randint, sample
from core.models import Portrait, SiteSettings


class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.tag

class Article(models.Model):
    headline = models.CharField(max_length=200)
    description_tag = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    pub_date = models.DateField()
    thumbnail = models.ImageField(blank=True, upload_to="blog_app/article/thumbnails")
    featured = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    article = fields.CKEditor5Field()
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
            while True:
                if not Article.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f"{self.slug}{randint(0,9)}"
        if not self.description_tag:
            self.description_tag = self.headline
        super(Article, self).save(*args, **kwargs)
    def __str__(self):
        return self.headline
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return SiteSettings.get().placeholder_thumbnail.url
    def get_related(self):
        current_article_tags = self.tags.all()
        related_articles = Article.objects.filter(tags__in=current_article_tags).exclude(id=self.id).exclude(active=False).distinct()
        return sample(list(related_articles), min(3, related_articles.count()))