from django_distill import distill_path
from . import views


app_name = "core"
urlpatterns = [
    distill_path("", views.HomeTemplateView.as_view(), name="home")
]