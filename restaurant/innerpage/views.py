from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import PrivacyPolicy
# Create your views here.

class InnerPage(TemplateView):
    template_name = 'innerpage/inner-page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['policy'] = PrivacyPolicy.objects.all()

        return context
