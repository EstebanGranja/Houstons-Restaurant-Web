# Generated by Django 4.1.4 on 2022-12-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_contact_face_contact_insta_contact_tw'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='google',
            field=models.URLField(blank=True, null=True, verbose_name='Google Maps link'),
        ),
    ]
