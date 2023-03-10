# Generated by Django 4.1.4 on 2022-12-22 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_staff_facebook_alter_staff_instagram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100, verbose_name='Event name')),
                ('price', models.IntegerField()),
                ('long_description', models.TextField(verbose_name='Long description')),
                ('event_image', models.ImageField(upload_to='events', verbose_name='Event image')),
            ],
            options={
                'ordering': ['price'],
            },
        ),
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(blank=True, help_text='600x600px approximately images recomended', null=True, upload_to='staff', verbose_name='Employee photo'),
        ),
    ]
