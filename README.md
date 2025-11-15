# Foodex Backend (Django + DRF + Channels)

Backend para el MVP de **Foodex** (recetas, pasos, ingredientes, inventario y sincronización en tiempo real).

## Stack
- Django 5
- Django REST Framework
- JWT (simplejwt)
- Channels + Redis (WebSockets)
- PostgreSQL

## Rápido inicio (sin Docker)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Edita credenciales de Postgres y Redis en .env

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# correr
python manage.py runserver
```

## Inicio con Docker (recomendado)
Necesitas Docker y Docker Compose.

```bash
cp .env.example .env
docker compose up -d --build
# Crea el superusuario dentro del contenedor:
docker compose exec web python manage.py createsuperuser
```

## Autenticación
- Obtener token: `POST /api/token/` → `{ "username": "...", "password": "..." }`
- Refrescar: `POST /api/token/refresh/`

## Endpoints principales
- `GET/POST /api/recetas/`
- `GET /api/recetas/{id}/scale?porciones=10`
- `GET /api/recetas/{id}/recalc-inventario?porciones=10`
- `GET/POST /api/ingredientes/`
- `GET/POST /api/pasos/`
- `GET/POST /api/canasta/`
- `GET /api/roles/` (POST/PUT solo Profesor/Admin)

## WebSocket
- URL: `ws://localhost:8000/ws/aula/<room>/`
- Enviar (profesor):
```json
{"type":"anotacion","autor":"chef","texto":"Corten brunoise"}
```
- Todos los clientes conectados al mismo `room` reciben el mensaje.

## Estructura
```
foodex-backend/
├─ foodex/ (settings del proyecto)
└─ core/   (app principal: modelos, vistas, serializers)
```

## Variables de entorno
Ver `.env.example`.

##Contribuir

Lee el archivo CONTRIBUTING.md para colaborar correctamente utilizando ramas y Pull Requests.
