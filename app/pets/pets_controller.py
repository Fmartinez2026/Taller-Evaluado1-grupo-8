from fastapi import APIRouter

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service
from app.shared.schemas import ApiResponse

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)

@router.get("", response_model=ApiResponse[list[Pet]])
def find_all(studentId: str):
    mascotas = pets_service.find_all_for_student(studentId)
    return ApiResponse.ok(
        status_code=200,
        message="Mascotas obtenidas exitosamente",
        data=mascotas
    )

@router.post("", status_code=201, response_model=ApiResponse[Pet])
def create(studentId: str, body: CreatePetDto):
    nueva_mascota = pets_service.create(studentId, body)
    return ApiResponse.ok(
        status_code=201,
        message="Mascota creada exitosamente",
        data=nueva_mascota
    )

@router.patch("/{petId}", response_model=ApiResponse[Pet])
def update(studentId: str, petId: str, body: UpdatePetDto):
    mascota_actualizada = pets_service.update(studentId, petId, body)
    return ApiResponse.ok(
        status_code=200,
        message="Mascota actualizada exitosamente",
        data=mascota_actualizada
    )

@router.delete("/{petId}", response_model=ApiResponse[Pet])
def delete(studentId: str, petId: str):
    mascota_eliminada = pets_service.delete(studentId, petId)
    return ApiResponse.ok(
        status_code=200,
        message="Mascota eliminada exitosamente",
        data=mascota_eliminada
    )
