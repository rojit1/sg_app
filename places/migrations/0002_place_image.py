# Generated by Django 3.1.4 on 2020-12-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/places/images'),
        ),
    ]
