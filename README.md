# 🧠 Quiz.AI - Sistema Inteligente de Cuestionarios con API REST y Frontend

Este proyecto implementa una **API RESTful con Django y Django REST Framework** para la gestión de cuestionarios, preguntas y opciones de respuesta, incluyendo un sistema de **evaluación automática con puntuación y retroalimentación**. Además, se añadió una interfaz **frontend simple con Bootstrap** para enviar respuestas desde un formulario web.

---

## 🚀 Tecnologías Usadas

- **Python 3.x**
- **Django 5.x**
- **Django REST Framework**
- **Bootstrap 5**
- **SQLite (por defecto)**
- **JSON API**

---

## ⚙️ Estructura del Proyecto (resumen)

La estructura principal del proyecto se encuentra dentro de la carpeta `src/`:

```
src/
│
├── quizzes/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── quizzes/
│   │       └── quiz_form.html
│   └── migrations/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

> Nota: los archivos y carpetas reflejan la implementación básica del sistema de quizzes. Puedes explorar `quizzes/` para ver modelos, serializers y vistas.

---

## 🧩 Funcionalidades Principales

1. **Gestión de Cuestionarios (Quizzes)**
   - Crear, listar, actualizar y eliminar quizzes.
2. **Gestión de Preguntas (Questions)**
   - Preguntas asociadas a un quiz.
3. **Gestión de Opciones (Choices)**
   - Opciones asociadas a una pregunta y bandera `is_correct` para evaluación.
4. **Evaluación Automática**
   - Validación de respuestas con cálculo de puntuación, porcentaje, calificación (grade), emoji y mensaje de retroalimentación.
5. **Frontend Interactivo**
   - Formulario web para enviar respuestas y visualizar resultados usando Bootstrap.

---

## 🔗 Endpoints Principales

Asumiendo prefijo `/api/v1/` en `config/urls.py` o `quizzes/urls.py`:

| Método | Endpoint | Descripción |
|:--:|:--|:--|
| `GET` | `/api/v1/` | Documentación general del API |
| `POST` | `/api/v1/quizzes/` | Crear un nuevo quiz |
| `GET` | `/api/v1/quizzes/` | Listar todos los quizzes |
| `GET` | `/api/v1/questions/` | Listar todas las preguntas |
| `POST` | `/api/v1/questions/` | Crear una nueva pregunta |
| `POST` | `/api/v1/choices/` | Crear opciones de respuesta |
| `GET` | `/api/v1/quizzes/<id>/` | Ver quiz completo con preguntas y opciones |
| `POST` | `/api/v1/quizzes/<id>/submit/` | Enviar respuestas y obtener calificación |
| `GET` | `/api/v1/quiz-form/` | Formulario web (frontend) para enviar respuestas |

> Nota: Ajusta rutas según la configuración real en `quizzes/urls.py`.

---

## 🧪 Ejemplos de Uso con `curl`

A continuación ejemplos para probar las APIs localmente (suponiendo servidor en `http://127.0.0.1:8000`):

### Crear un Quiz

```bash
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Python Basics 🐍", "description": "Test your Python knowledge"}'
```

### Crear una Pregunta

```bash
curl -X POST http://127.0.0.1:8000/api/v1/questions/ \
  -H "Content-Type: application/json" \
  -d '{"quiz": 1, "text": "What is Python?"}'
```

### Crear Opciones

```bash
curl -X POST http://127.0.0.1:8000/api/v1/choices/ \
  -H "Content-Type: application/json" \
  -d '{"question": 1, "text": "A programming language", "is_correct": true}'
```

### Enviar Respuestas (Evaluación Automática)

```bash
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/1/submit/ \
  -H "Content-Type: application/json" \
  -d '{
    "answers": [
      {"question_id": 1, "choice_id": 1},
      {"question_id": 2, "choice_id": 3}
    ]
  }'
```

Respuesta de ejemplo:

```json
{
  "quiz_title": "Python Basics 🐍",
  "total_questions": 2,
  "correct_answers": 2,
  "percentage": 100.0,
  "grade": "A",
  "emoji": "🏆",
  "message": "🏆 Outstanding! You got 2 out of 2 correct!"
}
```

---

## 🌐 Frontend (Formulario Web)

- Ruta del formulario (ejemplo): `http://127.0.0.1:8000/api/v1/quiz-form/`
- Archivo de plantilla: `quizzes/templates/quizzes/quiz_form.html`

En esta página podrás ingresar el ID del quiz, enviar las respuestas en formato JSON y ver los resultados con calificación y emojis.

Ejemplo del JSON esperado en el campo de respuestas:

```json
{
  "answers": [
    {"question_id": 1, "choice_id": 1},
    {"question_id": 2, "choice_id": 3}
  ]
}
```

---

## 🧾 Commits Clave (histórico sugerido)

- ✨ Inicialización del proyecto con Django y DRF
- 🧠 Creación de modelos `Quiz`, `Question` y `Choice`
- 🚀 Implementación de endpoints CRUD
- 🎯 Agregado sistema de validación y puntuación
- 🎨 Frontend con Bootstrap para envío de respuestas
- 🧾 Documentación completa y `README.md`

---

## 👩‍💻 Autor

Yamile Ochoa Marín
Estudiante de Ingeniería de Software
Proyecto: Quiz.AI - Sistema Inteligente de Evaluación
Tecsup – 2025

---

## 🏁 Cómo Ejecutar el Proyecto (instrucciones completas)

A continuación instrucciones para ejecutar localmente tanto en Windows como en Unix.

1. Clonar el repositorio

```powershell
git clone https://github.com/YamileOchoa/Django-QuizIA.git
cd src
```

2. Crear entorno virtual e instalar dependencias

Windows (PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Unix / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Migrar la base de datos

```powershell
python manage.py migrate
```

4. (Opcional) Crear superusuario para acceder al admin

```powershell
python manage.py createsuperuser
```

5. Ejecutar el servidor

```powershell
python manage.py runserver
```

6. Acceder a la API y frontend

- API: `http://127.0.0.1:8000/api/v1/`
- Formulario web: `http://127.0.0.1:8000/api/v1/quiz-form/`

---

## ✅ Pruebas sugeridas

- Prueba de creación de quiz, preguntas y choices mediante `curl` o Postman.
- Envío de respuestas a `/api/v1/quizzes/<id>/submit/` y verificación de la respuesta con puntuaciones.

---

## 🛠️ Mejoras y Siguientes Pasos (opcionales)

- Añadir autenticación (JWT / Token) y permisos por usuario.
- Añadir pruebas unitarias y de integración automatizadas (pytest / Django tests).
- Integración continua (GitHub Actions) para tests y linting.
- Mejorar UI del frontend, paginación y filtros en la API.
- Añadir endpoints para resultados históricos por usuario.

---

