from django.shortcuts import render
from rest_framework.viewsets import  ModelViewSet
from .models import ( Area, Construction_building, Construction_organization )
from .serializers import ( AreaSerializer, Construction_buildingSerializer, Construction_organizationSerializer)
from .permissions import ConstructPermission

class AreaAPIView(ModelViewSet):
    queryset=Area.objects.all()
    serializer_class=AreaSerializer
    permission_classes=[ConstructPermission]
    
    

class Construction_buildingAPIView(ModelViewSet):
    queryset=Construction_building.objects.all()
    serializer_class=Construction_buildingSerializer
    permission_classes=[ConstructPermission]
    



class Construction_organizationAPIView(ModelViewSet):
    queryset=Construction_organization.objects.all()
    serializer_class=Construction_organizationSerializer
    permission_classes=[ConstructPermission]        
    
    
    