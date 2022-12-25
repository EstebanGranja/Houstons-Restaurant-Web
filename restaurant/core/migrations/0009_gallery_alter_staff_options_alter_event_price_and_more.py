# Generated by Django 4.1.4 on 2022-12-22 21:07

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_event_alter_staff_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name_plural': 'Staff'},
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(verbose_name='Price (USD)'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(blank=True, help_text='600x600px approximately images recomended', null=True, upload_to=core.models.staff_upload_to, verbose_name='Employee photo'),
        ),
    ]
