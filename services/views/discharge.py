from django.shortcuts import render
from ..forms import DischargeForm, DischargeServiceForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from OPAL.models import Patient
from ..models import Discharge

@staff_member_required(login_url="/login/")
def discharge_create(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == "POST":
        form = DischargeForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.patient = patient
            task = form.save()
            return redirect("services:discharge_list", patient.id)
    else:
        form = DischargeForm()
    return render(request, "services/discharge/create.html", {"form":form, "patient": patient})

@staff_member_required(login_url="/login/")
def discharge_service_create(request, id):
    if request.method == "POST":
        form = DischargeServiceForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("services:discharge_create", id=id)
    else:
        form = DischargeServiceForm()
    return render(request, "services/discharge/discharge_service/create.html", {"form":form, "patient": Patient.objects.get(id=id)})

@staff_member_required(login_url="/login/")
def discharge_list(request, id):
    patient = Patient.objects.get(id=id)
    discharges = Discharge.objects.filter(patient=patient).order_by('-created_at')
    return render(request, "services/discharge/list.html", {"discharges":discharges, "patient": patient})

@staff_member_required(login_url="/login/")
def discharge_delete(request, id):
    discharge = Discharge.objects.get(id=id)
    discharge.delete()
    return redirect("OPAL:patient_single", id=discharge.patient.id)