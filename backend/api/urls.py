
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
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
route.register('personnels', PersonnelsViewSet)
route.register('groupes', GroupeViewSet)


urlpatterns = [
    path('', include(route.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
]
