from rest_framework.permissions import BasePermission, SAFE_METHODS


class ConstructPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
             return True
         
        if request.user.is_authenticated:
            return True 
        
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
             return True
        
        if request.user == obj.author or request.user.is_staff:
             return True 

