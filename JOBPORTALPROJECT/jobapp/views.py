from django.shortcuts import render,redirect
from jobapp.forms import Register
from jobapp.models import CityJobs,Apply
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
def welcome(request):
    return render(request,'jobapp/welcome.html')

def register(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'],first_name = data['first_name'],
                                            last_name = data['last_name'],email=data['email'],
                                            password=data['password'])
            return redirect('/accounts/login')
    return render(request,'jobapp/register.html',{'form':form})

@login_required
def index(request):
    user = request.user
    if request.method == 'POST':
        search = request.POST['search']
        city = CityJobs.objects.filter(Q(city__icontains = search)|Q(designation__icontains = search))
        return render(request,'jobapp/index.html',{'user':user,'city':city})
    else:
        return render(request,'jobapp/index.html',{'user':user})

@login_required
def apply(request,slug,designation,city):
    if request.method == 'POST':
        if not request.POST._mutable:
            request.POST._mutable = True
            request.POST['user'] = request.user
            user = Apply.objects.create(user = request.POST['user'],name =request.POST['uname'],
                                            age = request.POST['uage'],email = request.POST['uemail'],
                                            degree = request.POST['udegree'],college = request.POST['ucollege'],
                                            resume = request.POST['uresume'],company = slug,
                                            designation = designation,city = city)
            user.save()
            return redirect('/thanks')
    else:
        return render(request,'jobapp/apply.html')


@login_required
def thanks(request):
    return render(request,'jobapp/thanks.html')

def aboutus1(request):
    return render(request,'jobapp/aboutus1.html')

@login_required
def aboutus2(request):
    return render(request,'jobapp/aboutus2.html')

@login_required
def applied(request):
    applied = Apply.objects.filter(user__exact = request.user)
    return render(request,'jobapp/applied.html',{'applied':applied})

@login_required
def details(request,slug,designation,city):
    applied = Apply.objects.filter(user__exact = request.user,city__iexact = city)
    company_details = CityJobs.objects.filter(slug__iexact = slug,designation__iexact = designation,city__iexact = city)
    return render(request,'jobapp/details.html',{'company_details':company_details,'applied':applied})
