# Generated by Django 4.1.4 on 2022-12-23 19:18

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_testimonial_alter_gallery_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='whyus',
            name='submit',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to=core.models.gallery_upload_to),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Image order'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='job',
            field=models.CharField(max_length=30, verbose_name='Actual position / Job'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.testimonial_upload_to),
        ),
    ]
