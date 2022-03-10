from rest_framework import permissions

class UpdateOwnUserProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id  #returns a boolean value

class UpdateOwnUserStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id  #returns a boolean value
