# Generated by Django 3.0.8 on 2020-07-28 04:51

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_auto_20200728_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='note',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='note',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), default=None, max_length=6000, size=50),
        ),
    ]
