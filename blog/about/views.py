from django.views.generic import TemplateView
from .models import Certification, Tech
from core.models import SiteSettings


class AboutTemplateView(TemplateView):
    template_name = "about/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sitesettings"] = SiteSettings.get()
        context["techs"] = Tech.objects.all()
        context["certs"] = Certification.objects.all()
        return context