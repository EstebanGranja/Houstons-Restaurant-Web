# Generated by Django 4.1.4 on 2022-12-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_special_special_number_special_tab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='special',
            old_name='brief_description',
            new_name='description1',
        ),
        migrations.RenameField(
            model_name='special',
            old_name='real_description',
            new_name='description2',
        ),
        migrations.RemoveField(
            model_name='special',
            name='name',
        ),
        migrations.RemoveField(
            model_name='special',
            name='special_image',
        ),
        migrations.RemoveField(
            model_name='special',
            name='tab',
        ),
        migrations.AddField(
            model_name='special',
            name='description3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='special',
            name='description4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='special',
            name='description5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='special',
            name='special1',
            field=models.CharField(default='Special 1', max_length=50, verbose_name='Special 1'),
        ),
        migrations.AddField(
            model_name='special',
            name='special2',
            field=models.CharField(default='Special 2', max_length=50, verbose_name='Special 2'),
        ),
        migrations.AddField(
            model_name='special',
            name='special3',
            field=models.CharField(default='Special 3', max_length=50, verbose_name='Special 3'),
        ),
        migrations.AddField(
            model_name='special',
            name='special4',
            field=models.CharField(blank=True, help_text='Optional', max_length=50, null=True, verbose_name='Special 4'),
        ),
        migrations.AddField(
            model_name='special',
            name='special5',
            field=models.CharField(blank=True, help_text='Optional', max_length=50, null=True, verbose_name='Special 5'),
        ),
    ]