"""Job_Portal_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Job_Portal import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('home', views.home, name='home'),
    path('job_list', views.job_list,name='job_list'),
    path('job_list2', views.job_list2,name="job_list2"),
    path('job_list3', views.job_list3,name="job_list3"),
    path('login_form', views.login_form, name='login_form'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('candidate_data', views.candidate_data, name='candidate_data'),
    path('recruiter_data', views.recruiter_data, name='recruiter_data'),
    path('candidate_login', views.candidate_login, name='candidate_login'),
    path('recruiter_login', views.recruiter_login, name='recruiter_login'),
    path('recruiter_login_profile/<str:user>', views.recruiter_login_profile, name='recruiter_login_profile'),
    path('recruiter_home', views.recruiter_home, name='recruiter_home'),
    path('add_jobs', views.add_jobs, name='add_jobs'),
    path('Logout', views.Logout, name='Logout'),
    path('change_passwordCandidate', views.change_passwordCandidate, name='change_passwordCandidate'),
    path('userpasswordchange', views.userpasswordchange, name='userpasswordchange'),
    path('changepass_candidate', views.changepass_candidate, name='changepass_candidate'),
    path('recruiterprofile', views.recruiterprofile, name='recruiterprofile'),
    path('job_view/<int:pid>', views.job_view, name='job_view'),
    path('edit_jobdetail/<int:pid>', views.edit_jobdetail, name='edit_jobdetail'),
    path('candidate_profile/<str:user>', views.candidate_profile, name='candidate_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('job_details/<int:pid>', views.job_details, name='job_details'),
    path('apply_job/<int:pid>', views.apply_job, name='apply_job'),
    path('app_submit/<int:pid>', views.app_submit, name='app_submit'),
    path('footer', views.footer, name='footer'),
    path('searched_job', views.searched_job, name='searched_job'),
    path('category_job/<int:pid>', views.category_job, name='category_job'),
    path('candidate_applied', views.candidate_applied, name='candidate_applied'),
    path('candidate_view/<int:pid>', views.candidate_view, name='candidate_view'),
    path('candidate_detail/<int:pid>/<int:pid1>', views.candidate_detail, name='candidate_detail'),
    path('applied_job_list', views.applied_job_list, name='applied_job_list'),
    path('delete_job/<int:pid>', views.delete_job, name='delete_job'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

