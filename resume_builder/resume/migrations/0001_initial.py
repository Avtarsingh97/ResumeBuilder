# Generated by Django 5.0.1 on 2024-06-09 15:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('github_profile', models.URLField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('employment_dates', models.CharField(blank=True, max_length=100, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('institution_name', models.CharField(blank=True, max_length=100, null=True)),
                ('degree', models.CharField(blank=True, max_length=100, null=True)),
                ('attendance_dates', models.CharField(blank=True, max_length=100, null=True)),
                ('gpa', models.CharField(blank=True, max_length=10, null=True)),
                ('programming_languages', models.TextField(blank=True, null=True)),
                ('web_frameworks', models.TextField(blank=True, null=True)),
                ('databases', models.TextField(blank=True, null=True)),
                ('cloud_platforms', models.TextField(blank=True, null=True)),
                ('soft_skills', models.TextField(blank=True, null=True)),
                ('awards', models.TextField(blank=True, null=True)),
                ('projects', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
