from django.shortcuts import render
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'medipal_app/patient_list.html', {'patients': patients})

def pneumonia_detection(request):
    return render(request, 'medipal_app/pneumonia_detection.html')
def breast_cancer(request):
    return render(request, 'medipal_app/breast_cancer.html')
def kidney(request):
    return render(request, 'medipal_app/kidney.html')
def Heart(request):
    return render(request, 'medipal_app/Heart.html')
def Liver(request):
    return render(request, 'medipal_app/Liver.html')
def Malaria(request):
    return render(request, 'medipal_app/Malaria.html')
def Diabetes(request):
    return render(request, 'medipal_app/Diabetes.html')


def home(request):
    return render(request, 'medipal_app/home.html')
from allauth.account.views import SignupView
class RegisterView(SignupView):
    template_name = 'medipal_app/register.html'
# medipal_app/views.py

from django.shortcuts import render
from allauth.account.views import LoginView, SignupView

class CustomLoginView(LoginView):
    template_name = 'medipal_app/login.html'

class CustomSignupView(SignupView):
    template_name = 'medipal_app/register.html'
# accounts/views.py
# medipal_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# medipal_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'medipal_app/home.html'

class PneumoniaView(TemplateView):
    template_name = 'medipal_app/pneumonia.html'

class PatientListView(TemplateView):
    template_name = 'medipal_app/patient_list.html'

def pneumonia_detection(request):
    # Your pneumonia detection logic goes here
    return render(request, 'medipal_app/pneumonia_detection.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'medipal_app/register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'medipal_app/register.html', {'form': form})


# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
# medipal_app/views.py
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'medipal_app/login.html'
    success_url = reverse_lazy('home')  # Redirect to home after login

class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirect to home after logout

class CustomRegisterView(CreateView):
    template_name = 'medipal_app/register.html'
    form_class = register  # Replace with your actual registration form
    success_url = reverse_lazy('home')  # Redirect to home after registration


