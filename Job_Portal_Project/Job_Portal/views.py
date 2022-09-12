from django.shortcuts import render,redirect
from .models import *
from .models import Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from datetime import date
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def index(request):
    return render(request, 'index.html')


def footer(request):
    return render(request, 'footer.html')


def searched_job(request):
    if request.method == "POST":
         job_name = request.POST.get('job_name')
         loc_name = request.POST.get('loc_name')
         job_searched= Jobs.objects.filter(Q(title=job_name)|Q(location=loc_name))
         job_all = Jobs.objects.all()
         print(job_all)
         print(job_searched)
         d = {'job1': job_searched,'job2': job_all,'job_name':job_name}

         if not request.user.is_authenticated:
             return render(request, 'searched_job.html',d)
         else:
             return render(request, 'serached_job_login.html',d)
    else:
          return render(request, 'searched_job.html')


def home(request):
    if not request.user.is_authenticated:
        return redirect('login_form')
    data = Jobs.objects.all()

    data1 = Category.objects.all()
    no_job = Jobs.objects.all().count()
    no_company = RecruiterUser.objects.all().count()
    no_student = StudentUser.objects.all().count()

    d= {"job":data,"category": data1,"no_job":no_job,"no_company":no_company,"no_student":no_student}
    return render(request,'home.html',d)


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('login_form')
    user = request.user
    recruiter = RecruiterUser.objects.get(user=user)

    no_job = Jobs.objects.all().count()
    no_company = RecruiterUser.objects.all().count()
    no_student = StudentUser.objects.all().count()
    job = Jobs.objects.filter(recruiter=recruiter)
    d = {'job': job,"no_job":no_job,"no_company":no_company,"no_student":no_student}


    return render(request, 'recruiter_home.html',d)


def Logout(request):
    logout(request)

    return redirect('index')

def add_jobs(request):
    if not request.user.is_authenticated:
        return redirect('login_form')

    if request.method == "POST":

        start_date = request.POST.get('startdate')
        end_date = request.POST.get('enddate')
        title = request.POST.get('title')
        salary = request.POST.get('salary')
        description = request.POST.get('description')
        experience = request.POST.get('experience')
        location = request.POST.get('location')
        skills = request.POST.get('skills')
        job_type = request.POST.get('job_type')
        org_type = request.POST.get('org_type')
        name = Category.objects.all()
        dic = {"name": name}

        user = request.user
        recruiter = RecruiterUser.objects.get(user=user)

        Jobs.objects.create(recruiter=recruiter,company_name=recruiter.company_name,job_type=job_type,org_type=org_type,about_company = recruiter.about,start_date=start_date,end_date=end_date, title=title, salary=salary,company_logo = recruiter.recruiter_logo, description=description,  experience=  experience,location=location,skills=skills,creation_date=date.today())

        return redirect('job_list2')


    return render(request, 'add_jobs.html')


def job_list2(request):
    if not request.user.is_authenticated:
        return redirect('login_form')
    user = request.user
    recruiter = RecruiterUser.objects.get(user=user)
    job = Jobs.objects.filter(recruiter=recruiter)
    d = {'job': job}
    return render(request, 'job_list2.html',d)


def job_list(request):
    data = Jobs.objects.all()


    p =  Paginator(Jobs.objects.all(),1)
    page = request.GET.get('page')

    try:
        venues = p.get_page(page)

    except PageNotAnInteger:
        venues = all_post.page(1)

    except EmptyPage:
        venues = all_post.page(all_post.num_pages)



    data1 = {"job1": data,"venues":venues}

    return render(request, 'job_list.html',data1)

def job_list3(request):

    data = Jobs.objects.all()
    data1 = {"job1":data}

    return render(request, 'job_list3.html',data1)


def login_form(request):
    return render(request,"login_form.html")


def candidate_login(request):
    if request.method == "POST":

        u = request.POST['uname']
        p = request.POST['pass']
        user = authenticate(username=u, password=p)

        if user:
            user1 = StudentUser.objects.get(user=user)
            if user1.type == "candidate":
                login(request, user)
                return redirect("home")

            else:
                messages.success(request, "Account does not exist as a recruiter")
        else:
            messages.success(request, "Account does not exist")

    return render(request, "login_form.html")


def recruiter_login(request):
    if request.method == "POST":

        u = request.POST['uname']
        p = request.POST['pass']
        user = authenticate(username=u, password=p)

        if user:
           user1 = RecruiterUser.objects.get(user=user)
           if user1.type == "recruiter":
               login(request, user)
               messages.success(request, "Login Successfully")
               return redirect("recruiter_home")


           else:
               messages.success(request, "Account does not exist as a recruiter")

        else:
            messages.success(request, "Account does not exist")



    return render(request, "login_form.html")



def recruiter_login_profile(request,user):
    user1 = User.objects.get(username=user)
    user2 = RecruiterUser.objects.get(user=user1)


    if request.method == "POST":
        user1.first_name = request.POST.get('first_name')
        user1.last_name = request.POST.get('last_name')
        user2.establish_date = request.POST.get('establish_date')
        user2.company_name = request.POST.get('company_name')
        user2.recruiter_logo = request.FILES['company_logo']
        user2.mobile_no = request.POST.get('mobile_no')
        user2.address = request.POST.get('address')
        user2.about = request.POST.get('about')
        user2.save()
        user1.save()

        return redirect("login_form")

    return render(request, "recruiter_login_profile.html")


def user_profile(request):
    return render(request, "user_profile.html")


def candidate_data(request):

    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if password1 == password2:
        print("hello if1")
        if User.objects.filter(username=username).exists():
            print("hello if2")
            messages.success(request, "Account already exist")
            return redirect("user_profile")

        else:

            user = User.objects.create_user(username=username, email=username, password=password1)
            user.save()
            user = StudentUser.objects.create(user=user, password=password1, type="candidate")
            user.save()
            print('user created')
            return redirect('candidate_profile', user.user)
            

    else:
         messages.info(request, "password does not match")


    return render(request, "user_profile.html")


def recruiter_data(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


    if password1 == password2:
        print("hello if1")
        if User.objects.filter(username=username).exists():
            print("hello if2")
            messages.info(request, "Account already exist")
            return redirect('user_profile')

        else:
            print("hello else")
            user = User.objects.create_user(username=username, email=username, password=password1)
            user.save()
            user = RecruiterUser.objects.create(user=user, password=password1, type="recruiter",status="pending")
            user.save()

            return redirect("recruiter_login_profile",user.user)

    else:
        print("hello else2")
        messages.success(request, "password does not match")

    return render(request, "user_profile.html")
def change_passwordCandidate(request):
    return render(request,"change_passwordCandidate.html")

def userpasswordchange(request):
    if not request.user.is_authenticated:
        return redirect('login_form')

    if request.method =="POST":
        old_password=request.POST['current_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        u  = User.objects.get(id=request.user.id)
        if u.check_password(old_password):
            if password1 == password2:
                u.set_password(password1)
                u.save()
                print("password change successfully")

            else:
                print("new password not mathch")
        else:
            print(" old password does not match")

    return render(request,"login_form.html")


def changepass_candidate(request):
    return render(request,"changepass_candidate.html")


def recruiterprofile(request):
    if not request.user.is_authenticated:
        return redirect('login_form')
    user = request.user
    user1 = StudentUser.objects.get(user=user)
    profile ={'candidate': user1}
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        clg_name = request.POST.get('clg_name')
        course = request.POST.get('course')
        specialization = request.POST.get('specialization')
        joining_date = request.POST.get('joining_date')
        end_date = request.POST.get('end_date')

        user.last_name = last_name
        user.first_name = first_name
        user.date_of_birth = date_of_birth
        user.gender = gender
        user.mobile_no = mobile_no
        user.address = address
        user.clg_name = clg_name
        user.course = course
        user.specialization = specialization
        user.joining_date = joining_date
        user.end_date = end_date
        user.save()

    return render(request, "recruiterprofile.html", profile)


def edit_jobdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_form')
    job = Jobs.objects.get(id=pid)
    d = {'job': job}
    if request.method == "POST":

        start_date = request.POST.get('startdate')
        end_date = request.POST.get('enddate')
        title = request.POST.get('title')
        salary = request.POST.get('salary')
        description = request.POST.get('description')
        experience = request.POST.get('experience')
        location = request.POST.get('location')
        skills = request.POST.get('skills')
        job.title = title
        job.salary = salary
        job.experience = experience
        job.location= location
        job.skills = skills
        job.description =description
        job.save()
        try:

            if start_date or end_date:
                try:
                    job.start_date = start_date
                    job.end_date = end_date
                    job.save()
                    return redirect('job_list2')
                except:
                    pass
            else:
                pass

        except:
            return render(request, 'edit_jobdetail.html',job.id)

    return render(request,'edit_jobdetail.html',d)

def job_view(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_form')
    job = Jobs.objects.get(id=pid)
    d = {'job':  job}
    return render(request, "job_view.html", d)

def delete_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_form')
    job = Jobs.objects.get(id=pid)
    print(job)
    job.delete()
    job = Jobs.objects.get(id=pid)
    d = {'job': job}

    return render(request, "job_view.html", d)

def job_details(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_form')


    job = Jobs.objects.get(id=pid)
    d = {'jobdata': job}

    date1 = date.today()
    if request.method == 'POST':
        if job.end_date < date1:
            print("helloo guys")
            messages.success(request, "Application Closed")


        elif job.start_date > date1:
            print("helloo guys")
            messages.success(request, "Application Are not Open")

        else:
             return redirect('apply_job', pid)

    return render(request, "job_details.html", d)


def candidate_profile(request,user):
    print(user)
    user1 = User.objects.get(username=user)
    user2 = StudentUser.objects.get(user=user1)
    print(user1)

    if request.method == "POST":
        user1.first_name = request.POST.get('first_name')
        user1.last_name = request.POST.get('last_name')
        user2.date_of_birth = request.POST.get('date_of_birth')
        user2.gender = request.POST.get('gender')
        user2.mobile_no = request.POST.get('mobile_no')
        user2.address = request.POST.get('address')
        user2.candidate_logo = request.FILES['candidate_img']
        user2.clg_name = request.POST.get('clg_name')
        user2.course = request.POST.get('course')
        user2.specialization = request.POST.get('specialization')
        user2.joining_date = request.POST.get('joining_date')
        user2.end_date = request.POST.get('end_date')
        user2.save()
        user1.save()

        return redirect("login_form")

    return render(request, "candidate_profile.html")

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login_form')
    user = request.user
    user1 = RecruiterUser.objects.get(user=user)
    d = {'profile': user1}
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        establish_date = request.POST.get('establish_date')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        about = request.POST.get('about')
        user1.user.first_name= first_name
        user1.user.last_name = last_name
        user1.first_name = first_name
        user1.company_name = company_name
        user1.establish_date = establish_date
        user1.mobile_no = mobile_no
        user1.address = address
        user1.about = about
        user1.save()

    return render(request, "edit_profile.html",d)

def app_submit(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_form')

    user = request.user
    student = StudentUser.objects.get(user=user)
    job = Jobs.objects.get(id=pid)
    date1=date.today()
    if job.end_date < date1:
        messages.success(request, "Application Closed")
        return redirect('job_details', pid)



    elif job.start_date > date1:
        messages.success(request, "Application Are not Open")
        return redirect('job_details', pid)

    else:
        return redirect('apply_job', pid)


    return render(request, "job_details.html", profile)


def apply_job(request,pid):
   if request.method == "POST":
       r = request.FILES['resume']
       cover_letter = request.POST.get("cover_letter")
       hire_why = request.POST.get("hire_why")
       user1 = request.user
       student = StudentUser.objects.get(user=user1)
       job = Jobs.objects.get(id=pid)
       Apply.objects.create(job=job, student=student, resume=r,cover_letter = cover_letter,hire_why =hire_why ,apply_date=date.today())
       messages.success(request, "Application Send Successfully")

   return render(request, "apply_job.html")


def applied_job_list(request):
    user = request.user
    user1 = StudentUser.objects.filter(user=user)
    data = Apply.objects.filter(student=user1)
    p = Paginator(Jobs.objects.all(), 1)
    page = request.GET.get('page')

    try:
        venues = p.get_page(page)

    except PageNotAnInteger:
        venues = all_post.page(1)

    except EmptyPage:
        venues = all_post.page(all_post.num_pages)

    data1 = {"job1": data, "venues": venues}

    return render(request, 'applied_job_list.html', data1)




def category_job(request,pid):
     job2 = Jobs.objects.all()
     if pid == 1:
         job_searched = Jobs.objects.filter(Q(title__icontains='Engineer') | Q(description__icontains = 'Engineer'))
         n = Jobs.objects.filter(Q(title__icontains='Engineer') | Q(description__icontains='Engineer')).count()
         d = {'job1': job_searched,'num':n,'job2':job2}
         return render(request, 'serached_job_login.html', d)
     elif pid==2:
         job_searched = Jobs.objects.filter(Q(title__icontains='Scientist') | Q(description__icontains='Scientist'))
         n = Jobs.objects.filter(Q(title__icontains='Scientist') | Q(description__icontains='Scientist')).count()
         d = {'job1': job_searched, 'num': n,'job2':job2}
         return render(request, 'serached_job_login.html', d)
     elif pid==3:
         job_searched = Jobs.objects.filter(Q(title__icontains="Director") | Q(description__icontains='Director'))
         n = Jobs.objects.filter(Q(title__icontains="Director") | Q(description__icontains='Director')).count()
         d = {'job1': job_searched,'num':n,'job2':job2}
         return render(request, 'serached_job_login.html', d)
     elif pid==4:
         job_searched = Jobs.objects.filter(Q(title__icontains='Manager') | Q(description__icontains='Manager'))
         n = Jobs.objects.filter(Q(title__icontains='Manager') | Q(description__icontains='Manager')).count()
         d = {'job1': job_searched, 'num': n,'job2':job2}
         return render(request, 'serached_job_login.html', d)

     elif pid==5:
         job_searched = Jobs.objects.filter(Q(title__icontains='Specialist') | Q(description__icontains='Specialist'))
         n = Jobs.objects.filter(Q(title__icontains='Specialist') | Q(description__icontains='Specialist')).count()
         d = {'job1': job_searched, 'num': n,'job2':job2}
         return render(request, 'serached_job_login.html', d)

     elif pid==6:
         job_searched = Jobs.objects.filter(Q(title__icontains='Manager') | Q(description__icontains='Manager'))
         n = Jobs.objects.filter(Q(title__icontains='Manager') | Q(description__icontains='Manager')).count()
         d = {'job1': job_searched, 'num': n,'job2':job2}
         return render(request, 'serached_job_login.html', d)

     elif pid==7:
         job_searched = Jobs.objects.filter(Q(title__icontains='Consultant') | Q(description__icontains='Consultant'))
         n = Jobs.objects.filter(Q(title__icontains='Consultant') | Q(description__icontains='Consultant')).count()
         d = {'job1': job_searched, 'num': n,'job2':job2}
         return render(request, 'serached_job_login.html', d)

     elif pid==8:
         job_searched = Jobs.objects.filter(Q(title__icontains='Technology') | Q(description__icontains='Technology'))
         n = Jobs.objects.filter(Q(title__icontains='Technology') | Q(description__icontains='Technology')).count
         d = {'job1': job_searched, 'num': n,'job2':job2}
         return render(request, 'serached_job_login.html', d)

     return render(request,'serached_job.html')

def candidate_applied(request):
    if not request.user.is_authenticated:
        return redirect('login_form')
    user = request.user
    recruiter = RecruiterUser.objects.get(user=user)
    job = Jobs.objects.filter(recruiter=recruiter)
    num = []
    for i in job:

        numb = Apply.objects.filter(job=i).count()
        num.append(numb)
        print(numb)
    print(num)
    d = {"job":job,"num":num}
    return render(request, 'candidate_applied.html',d)


def candidate_view(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_form')
    print(pid)
    numb = Apply.objects.filter(job=pid)



    d = {"num": numb}
    return render(request, 'candidate_view.html',d)

def candidate_detail(request,pid,pid1):
    if not request.user.is_authenticated:
        return redirect('login_form')

    stu = StudentUser.objects.get(id=pid)
    job_de = Apply.objects.get(id=pid1)
    d = {'studata': stu,"job_de":job_de}

    return render(request, "candidate_detail.html", d)