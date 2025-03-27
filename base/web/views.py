from django.views.generic import TemplateView  # new

# Create your views here.
class HomeView(TemplateView):  # new
    template_name = "home/base.html"