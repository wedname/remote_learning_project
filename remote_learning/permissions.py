from rest_framework.permissions import BasePermission


class StudentOnly(BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and hasattr(request.user, "student")
                and request.user.is_active
                and request.user.is_student
        )


class TeacherOnly(BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and hasattr(request.user, "teacher")
                and request.user.is_active
                and request.user.is_teacher
        )
