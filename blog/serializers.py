from rest_framework import serializers
from .models import ( Area, Construction_building, Construction_organization )

class AreaSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Area
        fields='__all__'


class Construction_buildingSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Construction_building
        fields='__all__'
        

class Construction_organizationSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Construction_organization
        fields='__all__'        