from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect, render

from django.views.generic import CreateView, DetailView, UpdateView
from .models import User, Doctor, Patient, Consultation
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here
@login_required
def Home(request):
  
    context = {

        'doctors': Doctor.objects.all().count(),
        'patient': Patient.objects.all().count(),
       
        'patients': Patient.objects.all().order_by('-created')

    }
    return render(request,"sites/uses/index.html", context=context)

def DoctorList(request):
    context = {
        'doctors': Doctor.objects.all().order_by('-created')
    }
    return render(request,"sites/uses/doctor/liste.html", context=context)

@method_decorator([login_required], name='dispatch')
class PatientCreateView(CreateView):
    model = Patient
    template_name = "sites/uses/patient/add.html"

    fields = ['nom', 'prenom', 'age', 'sexe', 'profession', 'domicile', 'nationalite', 'referent', 
    'telephone', 'taille', 'poids', 'imc', 'asthme', 'epilepsie', 'drepanocytose', 'ulcere', 'sinusite',
     'diabete', 'hta', 'operation', 'gestite_parite', 'contraception', 'alcool', 'tabac', 'autre']

    def form_valid(self, form):
        user = form.save()
        return redirect('list-patient')

def AddDoctor(request):
    return render(request,"sites/uses/doctor/add.html")

@login_required
def PatientList(request):
    context = {
        'patients': Patient.objects.all().order_by('-created')
    }
    return render(request,"sites/uses/patient/liste.html", context=context)

@login_required
def create_consultation(request,pk):
    consulation = Consultation.objects.create(docteur_id=request.user.doctor.id, patient_id=pk)
    return redirect('consultation_do', pk=consulation.pk)

@method_decorator([login_required], name='dispatch')
class UpdateViewDetailView(UpdateView):
    model = Consultation
    template_name = "sites/uses/consultations/index.html"
    fields = ['motif_de_la_consultation', 'debut_de_la_maladie', 'signes_de_la_maladie', 
                'traitement_recu', 'evaluation', 'tension_arterielle', 'pouls', 'sao2', 
                'temperature', 'score_de_glasow', 'conjonctives', 'resume', 'hypothese_diagnostique', 
                'bilan_demande', 'diagnostic', 'traitement', 'evoluation', 'rendez_vous']

    def form_valid(self, form):
        user = form.save()
        return redirect('resume', pk=self.object.pk)

@login_required
def resume(request,pk):
    consultation ={ 'consultation': Consultation.objects.get(pk=pk)}
    return render(request,"sites/uses/consultations/resume.html", context=consultation)


@login_required
def historique(request,pk):
    context = {'patient' : Patient.objects.get(pk=pk)}
    return render(request,"sites/uses/patient/detail.html", context=context)

