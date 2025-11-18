from django.contrib import admin
from .models import (
    Role,
    User,
    Receta,
    Ingrediente,
    Etapa,
    RecetaEtapa,
    RecetaIngrediente,
    EtapaIngrediente,
    CategoriaIngrediente,
    Tecnica,
    RecetaTecnica,
)

from django.contrib import admin

from .models import (
    Role,
    User,
    CategoriaIngrediente,
    Ingrediente,
    Tecnica,
    Etapa,
    Receta,
    RecetaEtapa,
    RecetaIngrediente,
    EtapaIngrediente,
    RecetaTecnica,
)

admin.site.register(Role)
admin.site.register(User)
admin.site.register(CategoriaIngrediente)
admin.site.register(Ingrediente)
admin.site.register(Tecnica)
admin.site.register(Etapa)
admin.site.register(Receta)
admin.site.register(RecetaEtapa)
admin.site.register(RecetaIngrediente)
admin.site.register(EtapaIngrediente)
admin.site.register(RecetaTecnica)
