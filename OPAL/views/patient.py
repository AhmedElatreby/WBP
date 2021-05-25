from django.shortcuts import render
from .. models import Patient, Therapy
from .. forms import PatientForm
from django.db.models import Avg, Q
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

'''
    This view returns a single patinet object and the average
    direct and indirect times for therapies
'''
@login_required
def patient_single(request, id):
    patient = Patient.objects.get(id=id)
    therapies = Therapy.objects.filter(patient=id)
    indirect_average = therapies.aggregate(Avg('indirect_time'))
    direct_average = therapies.aggregate(Avg('direct_time'))
    return render(request, "OPAL/patient/single.html", {"patient": patient, "therapies": therapies, "direct_average": direct_average["direct_time__avg"], "indirect_average": indirect_average["indirect_time__avg"]})

'''
    The view returns a list of all patient before searching
'''
@login_required
def patient_list(request):
    return render(request, "OPAL/patient/list.html")


'''
    This view creating a patient object
'''
@staff_member_required(login_url="/login/")
def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("OPAL:patient_single", id=task.id)
    else:
        form = PatientForm()
    return render(request, "OPAL/patient/create.html", {"form":form})

'''
    This view editing a patient object
'''
@staff_member_required(login_url="/login/")
def patient_edit(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect("OPAL:patient_single", id=id)
    else:
        data = {"hospital_number": patient.hospital_number, "first_name": patient.first_name,
                "surname": patient.surname, "date_of_birth": patient.date_of_birth,
                "postcode": patient.postcode, "locality": patient.locality}
        form = PatientForm(initial=data)
    return render(request, "OPAL/patient/edit.html", {"form":form, "patient": patient})

'''
    This view deleting a patient object
'''
@staff_member_required(login_url="/login/")
def patient_delete(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('OPAL:patient_list')

'''
    This view searches for the patient object 
'''
@login_required
def patient_search(request):
    q = request.GET.get('q')
    messages = False
    object_list = Patient.objects.filter(
        Q(first_name__icontains=q) | Q(surname__icontains=q) | Q(hospital_number__icontains=q)
    )
    if len(object_list) == 0:
        messages = True
    return render(request, 'OPAL/patient/list.html', {"patients": object_list, "messages": messages})
