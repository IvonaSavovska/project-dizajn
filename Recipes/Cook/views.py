from django.shortcuts import render
from .models import Login
from .forms import LoginForm
# Create your views here.

def home(request):
    return render(request , "home.html")

def login(request):
    def login_view(request):
        form = AuthenticationForm()

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_student == True:
                ...
            # Return 401 if the user is None or the user is not a student
            return HttpResponse('Unauthorized', status=401)

        # Default HttpResponse on `GET` requests
        return render(request, 'login.html', {'form': form})

def healthybowl(request):
    return render(request, "healthybowl.html")

def salad(request):
    return render(request, "salad.html")

def meal(request):
    return render(request, "meal.html")


def birthday(request):
    return render(request, "birthday.html")

def christmas(request):
    return render(request, "christmas.html")

def newyear(request):
    return render(request, "newyear.html")


def mealplanner(request):
    return render(request, "mealplanner.html")

