from decimal import Decimal, ROUND_HALF_UP
from core.models.receta import Receta
from core.models.canasta import Canasta

def escalar_ingredientes(receta: Receta, porciones_objetivo: int):
    """
    Escala las cantidades de ingredientes de una receta según el número de porciones objetivo.
    Usa receta.porciones_base como referencia.
    """
    porciones_base = receta.porciones_base or 1
    factor = Decimal(porciones_objetivo) / Decimal(porciones_base)

    ingredientes_out = []
    for ing in receta.ingredientes.all():
        cantidad_escalada = (
            Decimal(ing.cantidad_base) * factor
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        ingredientes_out.append({
            "id": ing.id,
            "nombre_ing": ing.nombre_ing,
            "unidad": ing.unidad,
            "cantidad_original": float(ing.cantidad_base),
            "cantidad_escalada": float(cantidad_escalada),
        })

    return {
        "receta_id": receta.id,
        "nombre_receta": receta.nombre_receta,
        "porciones_base": porciones_base,
        "porciones_objetivo": porciones_objetivo,
        "factor": float(factor),
        "ingredientes": ingredientes_out,
    }


def reconciliar_con_inventario(receta: Receta, porciones_objetivo: int):
    """
    Compara lo que necesito vs lo que tengo en Canasta para una receta y porciones dadas.
    Devuelve:
    - ingredientes escalados
    - faltantes (si el stock es menor a lo requerido)
    """
    scaled = escalar_ingredientes(receta, porciones_objetivo)
    faltantes = []

    # Mapear por ingrediente
    for ing in receta.ingredientes.all():
        total_disponible = sum(
            Decimal(c.cantidad_disponible) for c in Canasta.objects.filter(ingrediente=ing)
        )

        porciones_base = receta.porciones_base or 1
        requerido = (
            Decimal(ing.cantidad_base)
            * Decimal(porciones_objetivo)
            / Decimal(porciones_base)
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        if total_disponible < requerido:
            faltantes.append({
                "ingrediente_id": ing.id,
                "nombre_ing": ing.nombre_ing,
                "unidad": ing.unidad,
                "requerido": float(requerido),
                "disponible": float(total_disponible),
                "faltante": float(requerido - total_disponible),
            })

    return {
        "scaled": scaled,
        "faltantes": faltantes,
    }
