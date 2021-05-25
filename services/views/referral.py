from django.shortcuts import render
from ..forms import ReferralForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from OPAL.models import Patient
from ..models import Referral

@staff_member_required(login_url="/login/")
def referral_create(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == "POST":
        form = ReferralForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.patient = patient
            task = form.save()
            return redirect("services:referral_list", patient.id)
    else:
        form = ReferralForm()
    return render(request, "services/referral/create.html", {"form":form, "patient": patient})

@staff_member_required(login_url="/login/")
def referral_list(request, id):
    patient = Patient.objects.get(id=id)
    referrals = Referral.objects.filter(patient=patient).order_by('-created_at')
    return render(request, "services/referral/list.html", {"referrals":referrals, "patient": patient})

@staff_member_required(login_url="/login/")
def referral_delete(request, id):
    referral = Referral.objects.get(id=id)
    referral.delete()
    return redirect("OPAL:patient_single", id=referral.patient.id)