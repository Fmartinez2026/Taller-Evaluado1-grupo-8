# CRUD Students & Pets (FastAPI)

Proyecto FastAPI que implementa un **CRUD en memoria** para la entidad `Student` y sus mascotas (`Pet`). No requiere base de datos ni contenedores: los datos viven en un diccionario dentro del servicio y se pierden al reiniciar la aplicación.

## Requerimientos

- Python 3.13+ (gestionado automáticamente por [uv](https://docs.astral.sh/uv/))
- uv

## Resumen funcional

La API expone operaciones CRUD completas:

- **Estudiantes** bajo `/api/students`:
    - **Crear**: `POST /api/students`
    - **Listar**: `GET /api/students`
    - **Buscar por id**: `GET /api/students/:id`
    - **Actualizar**: `PATCH /api/students/:id`
    - **Eliminar**: `DELETE /api/students/:id` (también elimina sus mascotas)
- **Mascotas** anidadas bajo `/api/students/:studentId/pets`:
    - **Listar**: `GET /api/students/:studentId/pets`
    - **Crear**: `POST /api/students/:studentId/pets`
    - **Actualizar**: `PATCH /api/students/:studentId/pets/:petId`
    - **Eliminar**: `DELETE /api/students/:studentId/pets/:petId`

Cada estudiante tiene `id` (UUID), `name`, `email`, `age`, `createdAt` y `updatedAt`. El `email` es único: se rechaza con `409 Conflict` si ya existe.

Cada mascota tiene `id` (UUID), `studentId`, `name`, `species`, `age` (opcional), `createdAt` y `updatedAt`. Solo puede operar sobre su estudiante dueño.

## Estándar de respuestas HTTP JSON

Todos los endpoints, tanto en respuestas exitosas como en errores controlables,
utilizan el tipo genérico `ApiResponse[T]`. El campo `data` puede representar un
objeto individual, una lista de objetos o información adicional de un error.

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `success` | `boolean` | Indica si la petición se procesó correctamente. |
| `statusCode` | `number` | Código de estado HTTP de la respuesta. |
| `message` | `string` | Mensaje legible que describe el resultado. |
| `data` | `T \| null` | Recurso, lista de recursos o detalles del error. |

Ejemplo de éxito (`201 Created`):

```json
{
  "success": true,
  "statusCode": 201,
  "message": "Estudiante creado exitosamente",
  "data": {
    "id": "uuid-del-estudiante",
    "name": "Ada Lovelace"
  }
}
```

Ejemplo de error (`404 Not Found`):

```json
{
  "success": false,
  "statusCode": 404,
  "message": "Estudiante no encontrado",
  "data": null
}
```

## Contexto técnico

- **Backend**: FastAPI
- **Almacenamiento**: en memoria (sin persistencia)
- **Validación**: Pydantic v2
- **Gestor de dependencias**: uv
- **Documentación**: Swagger en `/docs`

## Ejecución local

1. Instalar dependencias:

    ```bash
    make install
    ```

    O directamente con uv:

    ```bash
    uv sync
    ```

2. Levantar el servidor en modo desarrollo:

    ```bash
    make dev
    ```

    O usando uv:

    ```bash
    uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 3000
    ```

La aplicación queda disponible en:

- `http://localhost:3000`
- `http://localhost:3000/docs`

## Comandos útiles

- `make install` — sincroniza dependencias con uv
- `make dev` — arranca uvicorn en modo reload
- `make lint` — ejecuta Ruff (con autocorrección)
- `make format` — formatea el código con Ruff
- `make format-check` — verifica el formato
- `make clean` — elimina `.venv`, cachés y artefactos
