# Generated by Django 3.2.5 on 2021-09-04 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Portal', '0011_job_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_category',
            name='job',
        ),
    ]