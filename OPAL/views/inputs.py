from django.shortcuts import render
from ..models import Therapy, Therapist
from ..forms import DirectInputForm, IndirectInputForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from ..models import Patient

@staff_member_required(login_url="/login/")
def direct_input_create(request, id):
    if request.method == "POST":
        form = DirectInputForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("OPAL:therapy_create", id=id)
    else:
        form = DirectInputForm()
    return render(request, "OPAL/therapy/inputs/direct/create.html", {"form":form, "patient": Patient.objects.get(id=id)})


@staff_member_required(login_url="/login/")
def indirect_input_create(request, id):
    if request.method == "POST":
        form = IndirectInputForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("OPAL:therapy_create", id=id)
    else:
        form = IndirectInputForm()
    return render(request, "OPAL/therapy/inputs/indirect/create.html", {"form":form, "patient": Patient.objects.get(id=id)})
