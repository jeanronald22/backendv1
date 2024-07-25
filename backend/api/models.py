from django.db import models

from django.contrib.auth.models import User



class Personne(models.Model):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    
    def __str__(self) -> str:
        return self.user.username

class Information(models.Model):
    adresse = models.CharField(max_length=255)
    type_adresse = models.CharField(max_length=50)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name='informations')

class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    responsable = models.ForeignKey(Personne, on_delete=models.SET_NULL, null=True)

class Personnel(models.Model):
    personne = models.OneToOneField(Personne, on_delete=models.CASCADE)
    fonction = models.CharField(max_length=100)
    horaire_travail = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    specialites = models.CharField(max_length=255)

class Patient(models.Model):
    personne = models.OneToOneField(Personne, on_delete=models.CASCADE)
    temperature = models.FloatField()
    poids = models.FloatField()
    taille = models.FloatField()
    tension_art = models.FloatField()

class Facture(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    consultation = models.CharField(max_length=100)
    montant = models.FloatField()
    prestation = models.CharField(max_length=100)
    
class Consultation(models.Model):
    date_consultation = models.DateTimeField()
    symptoms = models.JSONField()
    diagnostic = models.TextField()
    
    def __str__(self) -> str:
        return self.diagnostic

class DossierMedical(models.Model):
    date_creation = models.DateField()
    date_modification = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name='dossiers_medical')
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='dossier_medical')

class GardeMalade(models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='garde_malade', null=True, blank=True)

class Prescription(models.Model):
    date = models.DateTimeField()
    service = models.CharField(max_length=100)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='prescriptions')

class Examen(models.Model):
    type_examen = models.CharField(max_length=100)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    date_realiser = models.DateTimeField()

class Operation(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Resultat(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    resultat = models.TextField()

class Diriger(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    poste = models.CharField(max_length=100)

class Rattacher(models.Model):
    infirmier = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)