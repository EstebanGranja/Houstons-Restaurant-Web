# Generated by Django 4.1.4 on 2022-12-23 20:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_text', ckeditor.fields.RichTextField(verbose_name='Privacy policy text')),
            ],
        ),
    ]