from django.shortcuts import render , redirect
from django.contrib.auth import login , logout ,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def sign_up(request):
    form = CustomUserCreationForm()
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            messages.success(request , f"Account was successfully for {user.username} !")
            login(request , user)
            send_mail(
                'Welcome to our site',
                f'We glad to have your company on board with us , make sure to stay up we will contact you soon !',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            return redirect("home")
        else:
            messages.error(request , "Error !")
    
    context = {
        "form" : form,
    }
    return render(request , "users/sign-up.html" , context)


def log_in(request):
    url = request.GET.get("next")
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.POST['next'] if 'next' in request.POST else 'home')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/log-in.html')

@login_required(login_url='log-in')
def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('log-in')

@login_required(login_url='log-in')
def my_profile(request , username):
    try : 
        user = User.objects.get(username = username)
        profile = Profile.objects.get(user = user)
        context = {
            "profile" : profile,
        }
        return render(request , "users/profile.html" , context)
    except :
        return redirect('make-profile')

@login_required(login_url='log-in')
def make_profile(request):
    form = ProfileForm()

    if request.method =="POST":
        try:
            form = ProfileForm(request.POST , request.FILES)
            profile = Profile()
            profile.user = request.user
            
            profile.avatar = request.FILES.get('avatar')
            profile.cover = request.FILES.get('cover')
            
            profile.name = request.POST.get('name')
            profile.phone = request.POST.get('phone1')
            profile.secondPhoneNumber = request.POST.get('phone2')
            profile.address = request.POST.get('address')
            profile.postcode = request.POST.get('postcode')
            profile.email = request.POST.get('email')
            profile.employees_number  = request.POST.get('nb_emp')
            profile.web_site = request.POST.get('website_url')
            profile.type = request.POST.get('type')
            
            profile.about_me = request.POST.get("about_me")
            print("###############"  , profile.about_me)
            
            profile.save()
            messages.success(request , f"Profile was successfully for {request.user.username} Check Your mail for more details !")
            #importing and seding mail
            send_mail(
                'Welcome to our site',
                f'We glad to have your company on board with us , make sure to stay up we will contact you soon on {profile.phone} .',
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,
            )
            
            return redirect("my-profile" , username=request.user.username)
        except :
            messages.error(request , "Error !")
    
    context = {
        "form":form,
    }
    return render(request , "users/make-profile.html" , context)