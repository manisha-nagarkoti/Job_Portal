# Generated by Django 3.2.5 on 2021-09-01 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Portal', '0007_auto_20210901_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiteruser',
            name='recruiter_logo',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='candidate_logo',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
