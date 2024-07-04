from django.urls import path, include
from .views import ( Construction_organizationAPIView, AreaAPIView, Construction_buildingAPIView)
from rest_framework import routers


router=routers.SimpleRouter()
router.register("area", AreaAPIView)
router.register("construction_organizationAPIView", Construction_organizationAPIView)
router.register("construction_buildingAPIView", Construction_buildingAPIView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
    
    
]
