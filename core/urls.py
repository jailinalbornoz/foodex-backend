from rest_framework.routers import DefaultRouter 
from .migrations.views.classCanastaViewSet import CanastaViewSet
from .migrations.views.classIngredienteViewSet import IngredienteViewSet
from .migrations.views.classPasoViewSet import PasoViewSet
from .migrations.views.classRecetaViewSet import RecetaViewSet
from .migrations.views.classRoleViewSet import RoleViewSet
from .migrations.views.classUserViewSet import UserViewSet


router = DefaultRouter()
router.register(r"roles", RoleViewSet)
router.register(r"users", UserViewSet, basename="users")
router.register(r"recetas", RecetaViewSet)
router.register(r"ingredientes", IngredienteViewSet)
router.register(r"pasos", PasoViewSet)
router.register(r"canasta", CanastaViewSet)

urlpatterns = router.urls
