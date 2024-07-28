from rest_framework import viewsets
from api.models import *
from api.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
# vu personne

class PersonneViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
class PersonnelsViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
class ServiceViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerialiser
    
class PatientViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientSerialiser
    
class ConsultationViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerialiser
    
class FactureViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Facture.objects.all()
    serializer_class = FactureSerialiser
    
class DossierMedicalViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = DossierMedical.objects.all()
    serializer_class = DossierMedicalSerialiser
    
    
#  vue d'optention des informations sur un  utilisateur connecte
class UserProfileView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        personnel = Personnel.objects.get(user=user)
        # personnel = Personnel.objects.filter(personne=personne).first()

        serializer = PersonnelSerializer(personnel)
        
        return Response(serializer.data)


class GroupeViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer