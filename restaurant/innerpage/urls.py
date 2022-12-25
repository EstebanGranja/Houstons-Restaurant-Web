from django.urls import path 
from .views import InnerPage

app_name = 'innerpage'
urlpatterns = [
    path('', InnerPage.as_view(), name='innerpage')
]