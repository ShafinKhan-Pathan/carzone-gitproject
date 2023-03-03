from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
#from django.contrib.auth.decorators import login_required
# Create your views here.
# If You want To not open Your Home Page You should have to do this
# @login_required(login_url = 'login')
def home(request):
    teams = Team.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car = Car.objects.order_by('-created_date')
    # We can also use this search_fields but by using this we are not getting the unique value
    # For example when i dropdown the values of year i get 2017 3 to 4 times so that's why we are using flat = True and .distinct() function as given example above
    #search_fields = Car.objects.values('model','city','year','body_style')
    model_search = Car.objects.values_list('model' , flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year' , flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat = True).distinct()


    data = {
        'teams':teams,
        'featured_car':featured_car,
        'all_car':all_car,
        #'search_fields':search_fields,
        'model_search':model_search,
        'city_search':city_search,
        'year_search' :year_search,
        'body_style_search':body_style_search,

    }
    return render(request , 'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'pages/about.html', data)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_message = 'You Have A New Message From Car Zone Check It'
        message_body = 'name :' +name+ ', email :' +email+ ', subject :' +subject+ ', phone :' +phone+ ' ,message :' +message

        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email


        send_mail(
            subject,
            message_body,
            'shafinkhanpathan2002@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        messages.success(request,'Thank You For Contact Us We Will Get Back To You Shortly .')

        return redirect('contact')




    return render(request , 'pages/contact.html')

def services(request):
    return render(request, 'pages/services.html')
