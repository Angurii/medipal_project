# medipal_app/urls.py

from django.urls import path
from .views import HomeView, PneumoniaView, PatientListView, pneumonia_detection, breast_cancer, kidney, Heart, Malaria, Diabetes, Liver
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
from .views import CustomLoginView, CustomRegisterView, CustomLogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pneumonia/', PneumoniaView.as_view(), name='pneumonia'),
    path('pneumonia_detection/', pneumonia_detection, name='pneumonia_detection'),
    path('breast_cancer/', breast_cancer, name= 'breast_cancer'),
    path('kidney/', kidney, name= 'kidney'),
    path('Heart/', Heart, name= 'Heart'),
    path('Liver/', Liver, name= 'Liver'),
    path('Malaria/', Malaria, name= 'Malaria'),
    path('Diabetes/', Diabetes, name= 'Diabetes'),
    path('patient_list/', PatientListView.as_view(), name='patient_list'),
    path('login/', LoginView.as_view(template_name='medipal_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Add logout view
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    # Add other URL patterns as needed
]

