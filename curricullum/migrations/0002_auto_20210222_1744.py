# Generated by Django 3.1.6 on 2021-02-22 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curricullum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='url',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='standard',
            old_name='url',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='url',
            new_name='slug',
        ),
    ]
