# Generated by Django 3.1.4 on 2020-12-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(null=True, upload_to='user_images'),
        ),
    ]
