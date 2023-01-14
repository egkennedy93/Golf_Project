from django.views.generic import TemplateView
from accounts.models import Golfer

class HomePage(TemplateView):
    template_name = 'index.html'
    extra_context={'golfers': Golfer.objects.all()}


class AboutPage(TemplateView):
    template_name = 'about.html'
    
