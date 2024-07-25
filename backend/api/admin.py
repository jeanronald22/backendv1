from django.contrib import admin
from api.models import *

# Register your models here.
class PersonneAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_naissance', 'sexe')
    search_fields = ('user__username', 'user__email')

class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('personne', 'fonction', 'service')
    search_fields = ('personne__user__username', 'fonction')
    list_filter = ('service',)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('personne', 'temperature', 'poids', 'taille', 'tension_art')
    search_fields = ('personne__user__username',)

class DossierMedicalAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medecin', 'date_creation', 'date_modification')
    search_fields = ('patient__personne__user__username', 'medecin__personne__user__username')
    list_filter = ('date_creation', 'date_modification')

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('date_consultation', 'diagnostic')
    search_fields = ('diagnostic',)
    list_filter = ('date_consultation',)

class FactureAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'consultation', 'montant', 'prestation')
    search_fields = ('patient__personne__user__username', 'consultation')
    list_filter = ('date',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'responsable')
    search_fields = ('nom', 'responsable__personne__user__username')

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('date', 'service', 'consultation')
    search_fields = ('service', 'consultation__diagnostic')
    list_filter = ('date',)

class ExamenAdmin(admin.ModelAdmin):
    list_display = ('type_examen', 'prescription', 'date_realiser')
    search_fields = ('type_examen', 'prescription__service')
    list_filter = ('date_realiser',)

class OperationAdmin(admin.ModelAdmin):
    list_display = ('prescription', 'date')
    search_fields = ('prescription__service',)
    list_filter = ('date',)

class ResultatAdmin(admin.ModelAdmin):
    list_display = ('prescription', 'resultat')
    search_fields = ('prescription__service', 'resultat')

class DirigerAdmin(admin.ModelAdmin):
    list_display = ('service', 'date_debut', 'date_fin', 'poste')
    search_fields = ('service__nom', 'poste')
    list_filter = ('date_debut', 'date_fin')

class RattacherAdmin(admin.ModelAdmin):
    list_display = ('infirmier', 'service', 'date_debut', 'date_fin')
    search_fields = ('infirmier__personne__user__username', 'service__nom')
    list_filter = ('date_debut', 'date_fin')

admin.site.register(Personne, PersonneAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(DossierMedical, DossierMedicalAdmin)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Facture, FactureAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Examen, ExamenAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Resultat, ResultatAdmin)
admin.site.register(Diriger, DirigerAdmin)
admin.site.register(Rattacher, RattacherAdmin)
