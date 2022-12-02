from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import post_save
from django.dispatch import receiver
import sys
from django.core.files import File
from datetime import datetime, date
from io import BytesIO
from django.urls import reverse

sexes = (
    ('Masculin ', 'Masculin',),
    ('Feminin', 'Feminin',),
)

sang = (
     ('A+', 'A+',),
     ('B+' , '+B',),
     ('O+' , 'O+',),
     ('AB+', 'AB+',),
     ('A-', 'A-',),
     ('B-' , 'B-',),
     ('O-' , 'O-',),
     ('AB-', 'AB-',),

)

status = (
     ('OUI', 'OUI',),
     ('NON' , 'NON',),
)

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)



class Doctor(models.Model):
    """Model definition for Doctor."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sexe = models.CharField(max_length=10, choices=sexes,)
    telephone  = models.CharField(max_length=10)
    groupe_sanguin = models.CharField(max_length=3, choices=sang,blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Doctor."""

        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        """Unicode representation of Doctor."""
        return "{} {}".format(self.user.last_name, self.user.first_name)


    def get_absolute_url(self):
        """Return absolute url for Doctor."""
        return ('')

    # TODO: Define custom methods here

  


class Patient(models.Model):

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sexe = models.CharField(max_length=10, choices=sexes,)
    profession = models.CharField(max_length=50)
    domicile = models.CharField(max_length=50)
    nationalite = models.CharField(max_length=50)
    referent = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    groupe_sanguin = models.CharField(max_length=3, choices=sang,blank=True, null=True)
    taille = models.CharField(max_length=50)
    poids = models.CharField(max_length=50)
    imc = models.CharField(max_length=50)
    asthme = models.CharField(max_length=3, choices=status,)
    epilepsie = models.CharField(max_length=3, choices=status,)
    drepanocytose = models.CharField(max_length=3, choices=status,)
    ulcere = models.CharField(max_length=3, choices=status,)
    sinusite = models.CharField(max_length=3, choices=status,)
    diabete = models.CharField(max_length=3, choices=status,)
    hta = models.CharField(max_length=3, choices=status,)
    operation = models.CharField(max_length=3, choices=status,)
    gestite_parite = models.CharField(max_length=50)
    contraception = models.CharField(max_length=3, choices=status,)
    alcool = models.CharField(max_length=3, choices=status,)
    tabac = models.CharField(max_length=3, choices=status,)
    autre = models.CharField(max_length=50, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


    class Meta:
        """Meta definition for Doctor."""

        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        """Unicode representation of Doctor."""
        return "{} {}".format(self.nom, self.prenom)

    @property
    def consultation(self):
        return self.patient_consultation.all().order_by('-created')


    @property
    def mat(self):
        a = str(self.created)
        return a[:14].replace(' ','DS').replace(':','').replace('-','')
    

class Consultation(models.Model):
    """Model definition for Consultation."""
    docteur = models.ForeignKey(Doctor, related_name="doctor_consultation", on_delete=models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient,related_name="patient_consultation",on_delete=models.CASCADE, blank=True, null=True)
    motif_de_la_consultation = models.TextField(blank=True)
    debut_de_la_maladie = models.CharField(max_length=50,blank=True)
    signes_de_la_maladie = models.CharField(max_length=100, blank=True)
    traitement_recu = models.TextField(blank=True)
    evaluation = models.TextField(blank=True)
    tension_arterielle  = models.IntegerField(default=0)
    pouls  = models.IntegerField(default=0)
    sao2  = models.IntegerField(default=0)
    temperature  = models.IntegerField(default=0)
    score_de_glasow  = models.IntegerField(default=0)
    conjonctives = models.IntegerField(default=0)
    resume = models.TextField(blank=True)
    hypothese_diagnostique = models.TextField(blank=True)
    bilan_demande = models.TextField(blank=True)
    diagnostic = models.TextField(blank=True)
    traitement = models.TextField(blank=True)
    evoluation = models.TextField(blank=True)
    rendez_vous = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Consultation."""

        verbose_name = 'Consultation'
        verbose_name_plural = 'Consultations'

    def __str__(self):
        """Unicode representation of Consultation."""
        return "{}".format(self.patient)


    def get_absolute_url(self):
        """Return absolute url for Consultation."""
        return ('')

    # TODO: Define custom methods here
