# Generated by Django 3.1.4 on 2020-12-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='category',
            field=models.ManyToManyField(to='places.Category'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='places'),
        ),
    ]
