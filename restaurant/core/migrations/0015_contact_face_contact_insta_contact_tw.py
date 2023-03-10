# Generated by Django 4.1.4 on 2022-12-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_contact_alter_about_image_alter_event_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='face',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook link'),
        ),
        migrations.AddField(
            model_name='contact',
            name='insta',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram link'),
        ),
        migrations.AddField(
            model_name='contact',
            name='tw',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter link'),
        ),
    ]
