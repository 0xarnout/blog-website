from django.utils import timezone
from django.http import Http404
from django.views.generic import DetailView, YearArchiveView
from .models import Article
from core.models import SiteSettings


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.filter(active=True)
    date_field = 'pub_date'
    make_object_list = True
    template_name = "blog_app/blog.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["sitesettings"] = SiteSettings.get()
        context['valid_years'] = Article.objects.filter(active=True, pub_date__lte=timezone.now().date()).values_list('pub_date__year', flat=True).distinct().order_by("-pub_date__year")
        context['current_year'] = self.get_year()
        return context

def ArticleHelperView(request):
    articles = Article.objects.filter(active=True, pub_date__lte=timezone.now().date())
    if articles.exists():
        last_year = articles.latest('pub_date').pub_date.year
        return ArticleYearArchiveView.as_view()(request, year=last_year)
    else:
        raise Http404

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog_app/article.html"
    def get_queryset(self):
        return self.model.objects.filter(active=True, pub_date__lte=timezone.now().date())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sitesettings"] = SiteSettings.get()
        return context