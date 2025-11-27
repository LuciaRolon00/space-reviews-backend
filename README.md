# 🚀 Space Reviews - Backend API

API REST desarrollada en Django para la plataforma **Space Reviews**, una comunidad de reseñas de videojuegos. Este proyecto gestiona la autenticación de usuarios, la base de datos de juegos y los mensajes de contacto.

## 🛠️ Tecnologías Utilizadas

* **Python & Django:** Framework principal.
* **Django REST Framework (DRF):** Para la creación de la API.
* **PostgreSQL:** Base de datos.
* **SQLite:** Base de datos (Local).
* **JWT (Simple JWT):** Autenticación segura por tokens.
* **Docker & Docker Compose:** Contención del entorno.
* **Gunicorn & Whitenoise:** Servidor de producción y gestión de archivos estáticos.

## ⚙️ Instalación y Ejecución Local

### Opción A: Con Docker
1.  Clonar el repositorio.
2.  Crear un archivo `.env` basado en las variables requeridas.
3.  Ejecutar:
    ```bash
    docker-compose up --build
    ```
4.  La API estará disponible en `http://localhost:8000`.

### Opción B: Manualmente
1.  Crear y activar un entorno virtual:
    ```bash
    python -m venv venv
    source venv/Scripts/activate # (Windows Git Bash)
    ```
2.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Aplicar migraciones:
    ```bash
    python manage.py migrate
    ```
4.  Iniciar servidor:
    ```bash
    python manage.py runserver
    ```

## ☁️ Despliegue
El proyecto está desplegado en **Render**.
* **URL Base:** `https://space-reviews-api.onrender.com/api`
* **Admin:** `https://space-reviews-api.onrender.com/admin`

---
*Proyecto realizado por Lucía Rolón para la Diplomatura Full Stack - UADE.*
