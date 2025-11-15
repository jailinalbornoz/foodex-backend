Guía para Contribuir al Proyecto FOODEx Backend

Gracias por colaborar 🎉
Sigue estas reglas para mantener el proyecto limpio, ordenado y profesional.

1. Requisitos previos

Python 3.10+

Git

Acceso como Collaborator en el repo

2. Flujo de trabajo Git (obligatorio)
SIEMPRE iniciar actualizando tu repo
git pull origin main

Crear una rama por funcionalidad
git checkout -b feature/nombre-funcion


Ejemplos:

feature/nueva-receta

fix/ingredientes-duplicados

Hacer commits pequeños y descriptivos
git add .
git commit -m "Agregado: endpoint de búsqueda de recetas"

Subir la rama
git push origin feature/nombre-funcion

Crear Pull Request (PR)

En GitHub:

Pull Requests → New Pull Request

Base: main

Compare: feature/nombre-funcion

Nadie hace push directo a main.

3. Estándares del backend

Código en inglés.

Modelos en singular (Receta, Ingrediente…).

Endpoints en plural (/recetas/, /ingredientes/…).

Lógica compleja → ir en services.py

No mezclar lógica de negocio dentro de views.

4. Estándares de seguridad

No subir .env

No subir db.sqlite3

No subir .venv

El .gitignore ya lo maneja.
