# Generated by Django 3.2.5 on 2021-09-04 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Portal', '0010_jobs_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job_Portal.jobs')),
            ],
        ),
    ]
