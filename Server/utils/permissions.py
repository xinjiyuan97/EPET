from rest_framework import permissions
from users.models import UserInfo

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 只有所有者可以修改
        if request.method in permissions.SAFE_METHODS:
            return True
        return str(obj.owner) == str(request.user)

class IsOwner(permissions.BasePermission):
    # 只有所有者可以读取和修改

    def has_object_permission(self, request, view, obj):
    

        return str(obj.owner) == str(request.user)

class IsTeacher(permissions.BasePermission):
    # 只有所有者可以读取和修改
    
    def has_object_permission(self, request, view, obj):
        userInfo = UserInfo.objects.get(userAccount = request.user)
        return userInfo.userType == 'TR'