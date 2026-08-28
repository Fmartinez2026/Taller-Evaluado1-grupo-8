from typing import Any, Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    success: bool
    statusCode: int
    message: str
    data: Optional[T] = None

    @classmethod
    def ok(
        cls, *, data: T, status_code: int = 200, message: str
    ) -> "ApiResponse[T]":
        return cls(
            success=True,
            statusCode=status_code,
            message=message,
            data=data,
        )

    @classmethod
    def error(
        cls, *, status_code: int, message: str, data: Any = None
    ) -> "ApiResponse[Any]":
        return cls(
            success=False,
            statusCode=status_code,
            message=message,
            data=data,
        )
