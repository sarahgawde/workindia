# Generated by Django 3.0.8 on 2020-07-27 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='firs_name',
            new_name='first_name',
        ),
    ]