from django.shortcuts import render,redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request , user)
            messages.success(request,"Your Are Successfully Logged In ! ")
            return redirect('dashboard')

        else:
            messages.error(request,"Invalid Credentials ")
            return redirect('login')


    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']# SHAFIN
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']


        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email Already Exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname , last_name=lastname , username = username , email = email , password = password)
                    # If you want to directly push your user to login page then use this code
                    #auth.login(request , user)
                    #messages.success(request,'You Are Now Logged In !')
                    #return redirect('dashboard')
                    user.save()
                    messages.success(request,'Registered Successfully !!')
                    return redirect('login')


        else:
            messages.error(request,'Password Is Not Similar')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

# Here I want That When The User Is Not Logged In Then I dont Want user to see the dashboard for that the following decorators we have to run


@login_required(login_url = 'login')

def dashboard(request):

    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)

    data = {
        'inquiries': user_inquiry,
    }
    return render(request,'accounts/dashboard.html',data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')
