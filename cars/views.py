from django.shortcuts import render , get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage , PageNotAnInteger, Paginator

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars , 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    # We can also use this search_fields but by using this we are not getting the unique value
    # For example when i dropdown the values of year i get 2017 3 to 4 times so that's why we are using flat = True and .distinct() function as given example above
    #search_fields = Car.objects.values('model','city','year','body_style')
    model_search = Car.objects.values_list('model' , flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year' , flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat = True).distinct()

    data = {
        'cars':paged_cars,
        #'search_fields':search_fields,
        'model_search':model_search,
        'city_search':city_search,
        'year_search' :year_search,
        'body_style_search':body_style_search,
    }

    return render(request, 'cars/cars.html',data)


def car_details(request , id):

    single_car = get_object_or_404(Car , pk=id)

    data = {
        'single_car':single_car,
    }

    return render(request,'cars/car_details.html', data)

def search(request):
    cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model' , flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year' , flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat = True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat = True).distinct()
# Ye keyword kaha se milega to hamara base.html me full page ka form hai vaha se milega {name  = "keyword" }
# sabse pahale to ham keyword ko check karenge ke kya keyword hai apne pass
# or agar he to apne uske variable ke ander store karva lenge as given in the second line
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
# here __icontains means we are searching for this keyword in the whole description when it finds the word it full that datas
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact = model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact = year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact = body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars =cars.filter(price__gte=min_price , price__lte=max_price)




    data = {
        'cars':cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search' :year_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search,

    }
    return render(request , 'cars/search.html',data)
