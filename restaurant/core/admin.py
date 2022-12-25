from django.contrib import admin
from .models import About, WhyUs, Special, Staff, Event, Gallery, Testimonial, Contact

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ['created']

class WhyUsAdmin(admin.ModelAdmin):
    list_display = ['number', 'short_title']
    readonly_fields = ['created']

class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'price']
    readonly_fields = ['created']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    readonly_fields = ['created']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'job']
    readonly_fields = ['created']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['order']
    readonly_fields = ['created']

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ['created']


admin.site.register(About, AboutAdmin)
admin.site.register(WhyUs, WhyUsAdmin)
admin.site.register(Special)
admin.site.register(Event, EventAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Contact, ContactAdmin)