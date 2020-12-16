from fastapi import APIRouter

from cadastro_usuarios.modules import healthcheck
from cadastro_usuarios.models.healthcheck import HealthcheckResponse, HEALTHCHECK_RESPONSE

router = APIRouter()


@router.get("/", response_model=HealthcheckResponse, status_code=200, summary="Informa o estado da API",
            responses=HEALTHCHECK_RESPONSE)
def listar():
    """
    O objetivo do endpoint é informar se a API está no ar, além disso, serve como \
    padrão para os demais endpoints.
    """
    return {"result": healthcheck.health_condition()}
