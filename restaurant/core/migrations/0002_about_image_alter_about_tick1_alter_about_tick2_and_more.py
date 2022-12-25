# Generated by Django 4.1.4 on 2022-12-22 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(null=True, upload_to='about'),
        ),
        migrations.AlterField(
            model_name='about',
            name='tick1',
            field=models.CharField(max_length=300, verbose_name='Tick 1'),
        ),
        migrations.AlterField(
            model_name='about',
            name='tick2',
            field=models.CharField(max_length=300, verbose_name='Tick 2'),
        ),
        migrations.AlterField(
            model_name='about',
            name='tick3',
            field=models.CharField(max_length=300, verbose_name='Tick 3'),
        ),
    ]