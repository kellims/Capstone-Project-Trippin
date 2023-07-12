# Generated by Django 4.2.3 on 2023-07-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reservation', models.URLField(blank=True, max_length=1000)),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
    ]
