# CRUD de Platos (Python)

API REST para gestionar platos usando FastAPI y SQLite.

## Requisitos

- Python 3.10+ instalado.

## Instalación

1. Crea y activa un entorno virtual.
2. Instala dependencias:
   - `pip install -r requirements.txt`

## Ejecución

- Inicia el servidor:
  - `uvicorn app.main:app --reload`
- La API queda disponible en:
  - `http://127.0.0.1:8000`
- Documentación interactiva:
  - `http://127.0.0.1:8000/docs`

## Endpoints

- `POST /platos`
- `GET /platos`
- `GET /platos/{plato_id}`
- `PUT /platos/{plato_id}`
- `DELETE /platos/{plato_id}`

## Pruebas

- Ejecuta:
  - `pytest`

## Notas

- La base de datos SQLite se crea en `platos.db` al ejecutar la app.
