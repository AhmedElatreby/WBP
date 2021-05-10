from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name

class Therapist(models.Model):

    # Enum for the therapist roles
    THERAPYASSISTANT = 'TA'
    OCCUPATIONTHERAPIST = 'OT'
    PHYSIOTHERAPY = 'PT'

    THERAPIST_ROLE_CHOICES = (
        (THERAPYASSISTANT, "Therapy Assistant"),
        (OCCUPATIONTHERAPIST, "Occupation Therapist"),
        (PHYSIOTHERAPY, "Physio Therapist"),
    )

    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    therapist_role = models.CharField(
        max_length=2,
        choices=THERAPIST_ROLE_CHOICES,
        default=THERAPYASSISTANT  
    )
    band = models.IntegerField(default=1)
    assigned_team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

class Patient(models.Model):
    hospital_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    postcode = models.CharField(max_length=8)
    locality = models.CharField(max_length=30)

    def __str__(self):
        return self.hospital_number

class DirectInput(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class IndirectInput(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Therapy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    rehab = models.BooleanField(default=False)
    direct_input = models.ForeignKey(DirectInput, blank=True, null=True, on_delete=models.SET_NULL)
    direct_time = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)
    indirect_input = models.ForeignKey(IndirectInput, blank=True, null=True, on_delete=models.SET_NULL)
    indirect_time = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Therapies"

    def __str__(self):
        return str(self.id)