from fastapi import APIRouter

from cadastro_usuarios.rotas.v1 import healthcheck, usuario, endereco


v1 = APIRouter()
v1.include_router(usuario.router, prefix="/usuario", tags=["usuario"])
v1.include_router(endereco.router, prefix="/endereco", tags=["endereco"])
v1.include_router(healthcheck.router, prefix="/health", tags=["healthcheck"])
