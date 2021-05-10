from django.shortcuts import render
from . models import Patient, Therapy, Therapist
from django.db.models import Avg

def patient_single(request, id):
    patient = Patient.objects.get(id=id)
    therapies = Therapy.objects.filter(patient=id)
    return render(request, "OPAL/patient/single.html", {"patient": patient, "therapies": therapies})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "OPAL/patient/list.html", {"patients": patients})

def therapy_single(request, id):
    therapy = Therapy.objects.get(id=id)
    return render(request, "OPAL/therapy/single.html", {"therapy": therapy})

def therapy_list(request):
    therapies = Therapy.objects.all()
    return render(request, "OPAL/therapy/list.html", {"therapies": therapies})

def therapist_list(request):
    therapist = Therapist.objects.all()
    return render(request, "OPAL/therapist/list.html", {"therapist": therapist})   

def therapist_single(request, id):
    therapist = Therapist.objects.get(id=id)
    therapies = Therapy.objects.filter(therapist=id)
    indirect_average = therapies.aggregate(Avg('indirect_time'))
    direct_average = therapies.aggregate(Avg('direct_time'))
    return render(request, "OPAL/therapist/single.html", {"therapist": therapist, "therapy": therapies, "direct_average": direct_average, "indirect_average": indirect_average})
 