# Generated by Django 4.2.3 on 2023-07-12 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='image',
            field=models.CharField(default='default_image.html', max_length=20000),
        ),
    ]
