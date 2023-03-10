# Generated by Django 4.1.4 on 2022-12-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField()),
                ('headline', models.CharField(max_length=200, verbose_name='About section headline')),
                ('subtitle', models.TextField()),
                ('tick1', models.TextField(verbose_name='Tick 1')),
                ('tick2', models.TextField(verbose_name='Tick 2')),
                ('tick3', models.TextField(verbose_name='Tick 3')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
    ]
