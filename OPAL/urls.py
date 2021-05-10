from django.urls import path, include
from . import views


urlpatterns = [
    path("patient/<int:id>/", views.patient_single, name="patient_single"),
    path("patient/", views.patient_list, name="patient_list"),
    path("therapist/<int:id>/", views.therapist_single, name="therapist_single"),
    path("therapist/", views.therapist_list, name="therapist_list"),
    path("therapy/<int:id>/", views.therapy_single, name="therapy_single"),
    path("therapy/", views.therapy_list, name="therapy_list"),
]