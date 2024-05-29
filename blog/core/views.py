from django.views.generic import TemplateView
from django.utils import timezone
from blog_app.models import Article
from .models import SiteSettings


class HomeTemplateView(TemplateView):
    template_name = "core/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sitesettings"] = SiteSettings.get()
        context["articles"] = Article.objects.filter(active=True, pub_date__lte=timezone.now().date(), featured=True).order_by("-pub_date")
        return context