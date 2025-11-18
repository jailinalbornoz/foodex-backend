from django.urls import path, include
from rest_framework.routers import DefaultRouter

# --- Views principales ---
from core.views.role_view import RoleViewSet
from core.views.user_view import UserViewSet
from core.views.ingrediente_view import IngredienteViewSet
from core.views.categoria_view import CategoriaIngredienteViewSet
from core.views.etapa_view import EtapaViewSet
from core.views.receta_view import RecetaViewSet
from core.views.tecnica_view import TecnicaViewSet
from core.views.canasta_view import CanastaViewSet

# --- Views de relaciones ---
from core.views.relaciones_view import (
    RecetaIngredienteViewSet,
    RecetaEtapaViewSet,
    RecetaTecnicaViewSet,
    EtapaIngredienteViewSet,
)

router = DefaultRouter()

# --------------------------
#     Usuarios y roles
# --------------------------
router.register(r'roles', RoleViewSet, basename='roles')
router.register(r'usuarios', UserViewSet, basename='usuarios')

# --------------------------
#     Catálogo base
# --------------------------
router.register(r'categorias', CategoriaIngredienteViewSet, basename='categorias')
router.register(r'ingredientes', IngredienteViewSet, basename='ingredientes')
router.register(r'etapas', EtapaViewSet, basename='etapas')
router.register(r'tecnicas', TecnicaViewSet, basename='tecnicas')
router.register(r'canastas', CanastaViewSet, basename='canastas')  # 👈 NUEVO

# --------------------------
#         Recetas
# --------------------------
router.register(r'recetas', RecetaViewSet, basename='recetas')

# --------------------------
#       Relaciones
# --------------------------
router.register(r'receta-ingredientes', RecetaIngredienteViewSet, basename='receta-ingredientes')
router.register(r'receta-etapas', RecetaEtapaViewSet, basename='receta-etapas')
router.register(r'receta-tecnicas', RecetaTecnicaViewSet, basename='receta-tecnicas')
router.register(r'etapa-ingredientes', EtapaIngredienteViewSet, basename='etapa-ingredientes')

urlpatterns = [
    path('', include(router.urls)),
]
