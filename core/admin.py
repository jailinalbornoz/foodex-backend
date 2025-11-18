from django.contrib import admin

from core.models.role import Role
from core.models.user import User
from core.models.ingrediente import CategoriaIngrediente, Ingrediente
from core.models.ingrediente import Ingrediente
from core.models.etapa import Etapa
from core.models.tecnica import Tecnica
from core.models.receta import Receta
from core.models.relaciones import (
    RecetaIngrediente,
    RecetaEtapa,
    RecetaTecnica,
    EtapaIngrediente,
)


admin.site.register(Role)
admin.site.register(User)
admin.site.register(CategoriaIngrediente)
admin.site.register(Ingrediente)
admin.site.register(Etapa)
admin.site.register(Tecnica)
admin.site.register(Receta)

admin.site.register(RecetaIngrediente)
admin.site.register(RecetaEtapa)
admin.site.register(RecetaTecnica)
admin.site.register(EtapaIngrediente)
