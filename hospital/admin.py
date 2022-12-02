from django.contrib import admin
from .models import  User, Doctor, Patient, Consultation
# Register your models here.

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = ('username','last_name', 'email','is_patient', 'is_doctor')

# register your models here.
@admin.register(Doctor)
class DocAdmin(admin.ModelAdmin):
    search_fields = ['user__username','user__first_name','user__last_name']
    list_display = ('user', 'sexe', 'telephone', 'groupe_sanguin', 'active', 'created', 'date_update', )

# register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    search_fields = ['nom', 'prenom']
    list_display = ('nom', 'prenom', 'age', 'sexe', 'profession', 'domicile', 'nationalite', 'referent', 'telephone', )

# register your models here.
@admin.register(Consultation)
class ConsultAdmin(admin.ModelAdmin):
    search_fields = ['nom', 'prenom']
    list_display = ('docteur', 'patient','rendez_vous', 'active', 'created', 'date_update', )