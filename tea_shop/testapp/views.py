from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def car_detail(request, car_id):
    context = {'car_id': car_id}
    return render(request, 'car_detail.html', context)

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def profile_view(request):
    return render(request, 'profile.html')
