from django.db.models.signals import post_migrate
from django.dispatch import receiver

from core.seeds import seed_roles, seed_admin


@receiver(post_migrate)
def ejecutar_seeds(sender, **kwargs):
    if sender.label == "core":
        print(" Ejecutando seeds...")
        seed_roles()
        seed_admin()
