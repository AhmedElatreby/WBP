from django.shortcuts import render
from ..models import Therapy, Patient, Therapist
from ..forms import TherapyForm
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

'''
    The view returns a list of all therapy input before searching
'''
@login_required
def therapy_single(request, id):
    therapy = Therapy.objects.get(id=id)
    return render(request, "OPAL/therapy/single.html", {"therapy": therapy})

'''
    The view returns a list of all therapy input related to a given
    patient
'''
@login_required
def therapy_list_patient(request, id):
    patient = Patient.objects.get(id=id)
    therapies = Therapy.objects.filter(patient=patient)
    return render(request, "OPAL/therapy/list.html", {"patient": patient, "therapies": therapies})

'''
    The view returns a list of all therapy input related to a given
    therapist
'''
@login_required
def therapy_list_therapist(request, id):
    therapist = Therapist.objects.get(id=id)
    therapies = Therapy.objects.filter(therapist=therapist)
    return render(request, "OPAL/therapy/list.html", {"therapist": therapist, "therapies": therapies})

'''
    The view create a therapy input 
'''
@staff_member_required(login_url="/login/")
def therapy_create(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == "POST":
        form = TherapyForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.patient = patient
            task = form.save()
            return redirect("OPAL:therapy_single", id=task.id)
    else:
        form = TherapyForm()
    return render(request, "OPAL/therapy/create.html", {"form":form, "patient": patient})

'''
    The view editing therapy input 
'''
@staff_member_required(login_url="/login/")
def therapy_edit(request, id):
    therapy = Therapy.objects.get(id=id)

    if request.method == "POST":
        form = TherapyForm(request.POST, instance=therapy)
        if form.is_valid():
            form.save()
            return redirect("OPAL:therapy_single", id=id)
    else:
        data = {"patient": therapy.patient, "therapist": therapy.therapist, 
                "rehab": therapy.rehab, "direct_input": therapy.direct_input, 
                "direct_time": therapy.direct_time, "indirect_input": therapy.indirect_input, "indirect_time": therapy.indirect_time}
        form = TherapyForm(initial=data)
    return render(request, "OPAL/therapy/edit.html", {"form":form, "therapy": therapy})

'''
    The view deleting therapy input 
'''
@staff_member_required(login_url="/login/")
def therapy_delete(request, id):
    therapy = Therapy.objects.get(id=id)
    therapy.delete()
    return redirect('OPAL:therapy_list')

'''
    The view searching for therapy input 
'''
@login_required
def therapy_search(request):
    q = request.GET.get('q')
    object_list = Therapy.objects.filter(
        Q(id__icontains=q) | Q(therapist__first_name__icontains=q) | Q(therapist__surname__icontains=q) | Q(patient__first_name__icontains=q) | Q(patient__surname__icontains=q)
    )
    return render(request, 'OPAL/therapy/list.html', {"therapies": object_list})
