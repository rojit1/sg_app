# Generated by Django 3.1.4 on 2020-12-31 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20201231_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='dob',
        ),
    ]
