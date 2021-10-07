# Generated by Django 3.1.6 on 2021-02-20 15:01

import app_users.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=150)),
                ('profile_pic', models.ImageField(blank=True, upload_to=app_users.models.path_and_rename, verbose_name='profile picture')),
                ('user_type', models.CharField(choices=[('student', 'student'), ('parent', 'parent'), ('teacher', 'teacher')], default='student', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]