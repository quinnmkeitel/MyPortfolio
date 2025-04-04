# Generated by Django 5.1.7 on 2025-03-26 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('entered_date', models.DateField()),
                ('finished_date', models.DateField()),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MyMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_name', models.CharField(max_length=100)),
                ('from_email', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('location', models.TextField(null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('summary', models.TextField(null=True)),
                ('photo', models.ImageField(null=True, upload_to='profile_pics')),
                ('major', models.CharField(max_length=100, null=True)),
                ('birthday', models.DateField(null=True)),
                ('website_url', models.URLField(null=True)),
                ('phone_number', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('github_url', models.URLField(max_length=100, null=True)),
                ('linkedin_url', models.URLField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('experience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience_item', to='MainApp.experience')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='MainApp.profile'),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100, null=True)),
                ('university', models.CharField(max_length=100)),
                ('entered_date', models.DateField()),
                ('graduation_date', models.DateField()),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='MainApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('image', models.ImageField(upload_to='profiles/')),
                ('github_url', models.URLField()),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='MainApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='MainApp.profile')),
            ],
        ),
    ]
