from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.
class PrivacyPolicy(models.Model):
    main_text = RichTextField(verbose_name='Privacy policy text')
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return 'Privacy Policy'

    class Meta:
        verbose_name_plural = 'Privacy Policy'
