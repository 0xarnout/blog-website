from django.utils import timezone
from django_distill import distill_path
from .models import Article
from . import views

def get_years():
    years = Article.objects.filter(active=True, pub_date__lte=timezone.now().date()).values_list('pub_date__year', flat=True).distinct()
    for year in years:
        yield {'year': year}

def get_articles():
    slugs = Article.objects.filter(active=True, pub_date__lte=timezone.now().date()).values_list('slug', flat=True)
    for slug in slugs:
        yield {'slug': slug}

app_name = "blog_app"
urlpatterns = [
    distill_path("", views.ArticleHelperView, name="blog"),
    distill_path("<int:year>.html", views.ArticleYearArchiveView.as_view(), name="articles", distill_func=get_years),
    distill_path("article-<slug:slug>.html", views.ArticleDetailView.as_view(), name="article", distill_func=get_articles),
]