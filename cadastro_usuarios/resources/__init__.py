from fastapi import APIRouter

from cadastro_usuarios.resources.v1 import healthcheck


v1 = APIRouter()
v1.include_router(healthcheck.router, prefix="/health", tags=["healthcheck"])
