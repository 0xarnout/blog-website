from django_distill import distill_path
from . import views


app_name = "about"
urlpatterns = [
    distill_path("", views.AboutTemplateView.as_view(), name="index")
]