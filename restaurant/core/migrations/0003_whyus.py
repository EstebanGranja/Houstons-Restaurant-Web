# Generated by Django 4.1.4 on 2022-12-22 14:35

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_about_image_alter_about_tick1_alter_about_tick2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=builtins.id)),
                ('reason', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Why us',
            },
        ),
    ]
