from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
from django import forms
# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate_logo = models.ImageField(null=True,upload_to="images/")
    date_of_birth = models.DateField(default=timezone.now, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, null=True)
    password = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=60,null=True)
    type = models.CharField(max_length=15, null=True)
    course= models.CharField(max_length=15, null=True)
    specialization = models.CharField(max_length=15, null=True)
    clg_name = models.CharField(max_length=15, null=True)
    joining_date = models.DateField(default=timezone.now, blank=True, null=True)
    end_date = models.DateField(default=timezone.now, blank=True, null=True)

    def _str_(self):
        return self.user.username


class Category(models.Model):

    name = models.CharField(max_length=30)


    def _str_(self):
        return self.name



class RecruiterUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=15, null=True)
    establish_date = models.DateField(default=timezone.now, blank=True, null=True)
    recruiter_logo = models.FileField(null=True,upload_to="images/")
    about = models.CharField(max_length=1000, null=True)
    password = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=60, null=True)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=20, null=True)

    def _str_(self):
        return self.user.username


class Jobs(models.Model):
    recruiter = models.ForeignKey(RecruiterUser, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now, blank=True, null=True)
    end_date = models.DateField(default=timezone.now, blank=True, null=True)
    company_name = models.CharField(max_length=15, null=True)
    about_company = models.CharField(max_length=1000,null=True)
    company_logo = models.FileField(null=True, upload_to="images/")
    title = models.CharField(max_length=50)
    salary = models.CharField(max_length=60)
    description = models.CharField(max_length=1000)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=110)
    job_type = models.CharField(max_length=110, null=True)
    org_type =  models.CharField(max_length=110, null=True)
    creation_date = models.DateField(default=timezone.now, blank=True, null=True)


    def _str_(self):
        return self.title

class Apply(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    apply_date = models.DateField(default=timezone.now, blank=True, null=True)
    resume = models.FileField(null=True)
    cover_letter = models.CharField(max_length=500, null=True)
    hire_why = models.CharField(max_length=500, null=True)



    def _str_(self):
        return self.id

class Save_job(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)


    def _str_(self):
        return self.id
