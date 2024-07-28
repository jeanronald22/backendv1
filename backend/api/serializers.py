from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *

# definition des different serialisers
#  serialiser de User 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
# group 
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
# definition du serialiser de personne
class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = '__all__'
        
    # redefinition de la methode create( ) pour permettre a django de connaitrement comment il vas creer un nouvelle utilisateur 
    def create(self, validated_data):
        user_info = validated_data.pop('user') # recuperation ders information des user
        user = User.objects.create_user(**user_info) # creation d'un user
        personne = Personne.objects.create(user=user, **validated_data) # creation de la personne avec le user en tant qu'attribut
        return personne
    
    # redefinition de la methode update( ) pour permettre a django de connaitre comment il vas mettre a jour les informations d'une personne
    def update(self, instance, validated_data): #instance: instance a mettre a jour 
        user_data = validated_data.pop('user', None) # Récupération des données utilisateur
        for attr, value in validated_data.items(): # Mise à jour des données de la personne
            setattr(instance, attr, value)
        instance.save()
        
        # Mise à jour des données utilisateur
        if user_data:
            user = instance.user
            for attr, value in user_data.items():
                if attr == 'password':
                    user.set_password(value)  # Mettre à jour le mot de passe
                else:
                    setattr(user, attr, value)
            user.save()

        return instance
    
#-------------------------------------------------------------- Serialiser/endpoint Service --------------------------------#
#-----------------------------------------------operations possible sur tous les service (get, update, delete) -------------#

class ServiceSerialiser(serializers.ModelSerializer):
    responsable = serializers.PrimaryKeyRelatedField(queryset=Personnel.objects.all(), required=False)
    class Meta:
        model = Service
        fields = '__all__'
    def create(self, validated_data):
        # Création du service avec le responsable référencé
        service = Service.objects.create(**validated_data)
        return service

    def update(self, instance, validated_data):
        # Mise à jour des attributs du service
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
#-------------------------------------------------------------- Serialiser/endpoint Patient --------------------------------#
#-----------------------------------------------operations possible sur tous les Patient (get, update, delete) -------------#

class PatientSerialiser(serializers.ModelSerializer):
    personne = PersonneSerializer(required=True)
    
    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        personne_info = validated_data.pop('personne', None) 
        if personne_info:
            personne = Personne.objects.create(**personne_info)
        patient = Patient.objects.create(personne = personne, **validated_data)
        return patient

    def update(self, instance, validated_data):
        # Mise à jour des attributs du patient
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
#-------------------------------------------------------------- Serialiser/endpoint consultation --------------------------------#
#-----------------------------------------------operations possible sur tous les consultations (get, update, delete) -------------#

class ConsultationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'
        
#-------------------------------------------------------------- Serialiser/endpoint Facture --------------------------------#
#-----------------------------------------------operations possible sur tous les Facture (get, update, delete) -------------#


class FactureSerialiser(serializers.ModelSerializer):
    consultation = serializers.PrimaryKeyRelatedField(queryset=Consultation.objects.all(), required=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), required=True)
    class Meta:
        model = Facture
        fields = '__all__'
    
    def create(self, validated_data):
        consultation_data = validated_data.pop('consultation', None)
        patient_data = validated_data.pop('patient', None)
        personne_data = patient_data.pop('personne', None) # oin extraire les donnee de la personne du patient
        user_info = personne_data.pop('user', None) # extraction des info d'un user de ;la personne
        
        # creation des different profiles
        if consultation_data:
            consultation = Consultation.objects.create(**consultation_data)
        if user_info:
            user = User.objects.create_user(**user_info)
            personne = Personne.objects.create(user=user, **personne_data)
            patient = Patient.objects.create(personne=personne, **patient_data)
        facture = Facture.objects.create(consultation=consultation, patient=patient, **validated_data)
        return facture
        
#-------------------------------------------------------------- Serialiser/endpoint Dossier medical --------------------------------#
#-----------------------------------------------operations possible sur tous les Dossiers medicaux (get, update, delete) -------------#

class DossierMedicalSerialiser(serializers.ModelSerializer):
    
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    medecin = serializers.PrimaryKeyRelatedField(queryset=Personnel.objects.all())
    consultation = serializers.PrimaryKeyRelatedField(queryset=Consultation.objects.all())
    
    class Meta:
        model = DossierMedical
        fields = '__all__'

    def create(self, validated_data):
        # Création du dossier médical
        dossier_medical = DossierMedical.objects.create(**validated_data)
        return dossier_medical

    def update(self, instance, validated_data):
        # Mise à jour des attributs du dossier médical
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
#-------------------------------------------------------------- Serialiser/endpoint Personnel --------------------------------#
#-----------------------------------------------operations possible sur tous le Personnelx (get, update, delete) -------------#

class PersonnelSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    patient = PatientSerialiser(required=False)

    class Meta:
        model = Personnel
        fields = '__all__'
    
    def create(self, validated_data):
        # Création du personnel avec le user référencé
        user_info = validated_data.pop('user', None)
        patient_info = validated_data.pop('patient', None)
        personne_data = patient_info.pop('personne', None)
        if user_info:
            user = User.objects.create_user(**user_info)
        if patient_info:
            personne = Personne.objects.create(**personne_data)
            patient = Patient.objects.create(personne = personne, **patient_info)
        personnel = Personnel.objects.create(user=user, patient=patient, **validated_data)
        return personnel
