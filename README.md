# 🍽️ Foodex Backend  
Backend profesional para el sistema Foodex — plataforma académica para gestión de recetas, ingredientes, técnicas culinarias y control de inventario para estudiantes de gastronomía.

Construido con **Django + Django REST Framework + JWT + Swagger** bajo una arquitectura modular y escalable.

---

## 🚀 Tecnologías principales

| Componente | Tecnología |
|-----------|------------|
| Backend | Django 5 + DRF |
| Auth | JWT (SimpleJWT) |
| Documentación | Swagger (drf-yasg) |
| Base de datos | PostgreSQL (producción) / SQLite (desarrollo) |
| WebSockets | Django Channels + Redis | --- pendiente
| Seeds automáticos | Signals + seeds.py |
| Control de roles | Admin / Profesor / Alumno |

---

# 📁 Estructura del Proyecto

foodex-backend/
│── core/
│ ├── models/
│ ├── serializers/
│ ├── views/
│ ├── permissions.py
│ ├── services.py
│ ├── seeds.py
│ ├── signals.py
│ └── urls.py
│
├── foodex/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── manage.py
└── README.md

Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

3️⃣ Instalar dependencias
pip install -r requirements.txt

🔑 Variables de Entorno (.env)

Crear archivo .env en la raíz:

SECRET_KEY=super-secreto
DEBUG=1

# PostgreSQL (opcional)
DB_NAME=foodex
DB_USER=postgres
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=5432

# Redis
REDIS_URL=redis://127.0.0.1:6379/0


Si no tienes PostgreSQL, el proyecto usa SQLite automáticamente.

🛠️ Migraciones
python manage.py makemigrations
python manage.py migrate

🌱 Seeds automáticos

Los seeds se ejecutan después de cada migrate (via signals):

Incluye:

Roles iniciales (Admin, Profesor, Alumno)

Usuario administrador inicial (correo: admin@foodex.cl
)

Si quieres ejecutarlos manualmente:

python manage.py shell
>>> from core.seeds import seed_roles, seed_admin
>>> seed_roles()
>>> seed_admin()

👤 Crear Superusuario
python manage.py createsuperuser

🔐 Autenticación (JWT)
Endpoint para obtener tokens:
POST /api/v1/auth/login/


Request:

{
  "correo_electronico": "admin@foodex.cl",
  "password": "admin123"
}


Respuesta:

{
  "access": "token...",
  "refresh": "token..."
}


Colocar el access token en Swagger y Postman:

Authorization: Bearer <token>

📘 Swagger – Documentación API

Abrir en el navegador:

👉 http://127.0.0.1:8000/api/docs/

Se genera automáticamente con todas tus rutas, modelos y schemas.

📦 Endpoints principales
Usuarios y roles
GET/POST     /api/v1/usuarios/
GET          /api/v1/roles/

Ingredientes / Categorías
GET/POST     /api/v1/ingredientes/
GET/POST     /api/v1/categorias/

Recetas (CRUD + extras)
GET/POST     /api/v1/recetas/
GET          /api/v1/recetas/{id}/detalle_completo/
GET          /api/v1/recetas/{id}/recalcular?porciones=10
GET          /api/v1/recetas/buscar?q=salsa
GET          /api/v1/recetas/por_categoria?id_categoria=1
GET          /api/v1/recetas/por_tecnica?id_tecnica=2

Canasta (stock)
GET/POST    /api/v1/canasta/

🧠 Permisos por Rol
Rol	Permisos
Admin	CRUD total
Profesor	Lectura + crear recetas + editar limitados
Alumno	Solo lectura

Se controla mediante:

core/permissions.py

🔥 Comandos útiles
Correr servidor
python manage.py runserver

Limpiar base de datos SQLite
rm db.sqlite3
rm core/migrations/00*.py
python manage.py makemigrations
python manage.py migrate

Contribución

Pull requests y sugerencias son siempre bienvenidas ✨
Si deseas extender el backend, contacta a tu equipo de desarrollo.