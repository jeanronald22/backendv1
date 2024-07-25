
from django.urls import path, include
from rest_framework import routers
from api.views import *

# definition du routeurs
route = routers.DefaultRouter()

# enregistrement des route
route.register('personnes', PersonneViewSet)
route.register('services', ServiceViewSet)
route.register('patients', PatientViewSet)
route.register('consultations', ConsultationViewSet)
route.register('factures', FactureViewSet)
route.register('dossiers_medical', DossierMedicalViewSet)


urlpatterns = [
    path('', include(route.urls))
]
