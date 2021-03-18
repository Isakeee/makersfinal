from rest_framework import permissions


class ProductPermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        print(obj.seller)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.seller == request.user