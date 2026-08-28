from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.pets.pets_controller import router as pets_router
from app.students.students_controller import router as students_router
from app.shared.schemas import ApiResponse


def create_app() -> FastAPI:
    app = FastAPI(
        title="Taller 1 - CRUD Students & Pets",
        description="API de un CRUD en memoria para la entidad Student y sus mascotas (Pet)",
        version="1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        body = ApiResponse[None](
            success=False,
            statusCode=exc.status_code,
            message=str(exc.detail),
            data=None
        )
        return JSONResponse(status_code=exc.status_code, content=body.model_dump())

    app.include_router(students_router)
    app.include_router(pets_router)

    return app


app = create_app()