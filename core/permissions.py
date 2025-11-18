from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated 
            and request.user.role 
            and request.user.role.nombre_rol == "Admin"
        )

class IsProfesor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role
            and request.user.role.nombre_rol == "Profesor"
        )

class IsAlumno(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role
            and request.user.role.nombre_rol == "Alumno"
        )

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated 
            and request.user.role.nombre_rol == "Admin"
        )

class IsProfesorOrAdmin(BasePermission):
    """
    Profesores pueden crear y editar recetas.
    Admin puede todo.
    Alumnos solamente lectura.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated or not request.user.role:
            return False

        return request.user.role.nombre_rol in ["Admin", "Profesor"]
