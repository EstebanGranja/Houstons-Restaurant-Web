from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import About, WhyUs, Special, Staff, Event, Gallery, Testimonial, Contact
# Create your views here.

class CoreView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all()
        context['reasons'] = WhyUs.objects.all()
        context['specials'] = Special.objects.all()
        context['staff'] = Staff.objects.all()
        context['events'] = Event.objects.all()
        context['gallery'] = Gallery.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['contacts'] = Contact.objects.all() 
        
        return context