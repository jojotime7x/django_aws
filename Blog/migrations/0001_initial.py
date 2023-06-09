# Generated by Django 3.2.5 on 2023-04-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookOrCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('producername', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.CharField(choices=[('ADVANCED', 'Advanced'), ('INTERMEDIATE', 'Intermediate'), ('INCIPIANTE', 'Incipiante')], max_length=50, null=True)),
                ('rec_type', models.CharField(choices=[('COURSE', 'Course'), ('BOOK', 'Book')], max_length=50, null=True)),
                ('estimatedtimetocomplete', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
