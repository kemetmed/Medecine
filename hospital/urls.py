from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name="home"),
    path('doctors/add/', AddDoctor,name="add-doctor"),
    path('doctors/list/', DoctorList,name="list-doctor"),
    path('patients/add/', PatientCreateView.as_view(),name="add-patient"),
    path('patients/list/', PatientList,name="list-patient"),
    path('create_consultation/<int:pk>/', create_consultation,name="consultation_create"),
    path('do_consultation/<int:pk>/', UpdateViewDetailView.as_view(),name="consultation_do"),
    path('resume_consultation/<int:pk>/',resume ,name="resume"),
    path('users/histories/<int:pk>/',historique ,name="historique"),

    
    
]
