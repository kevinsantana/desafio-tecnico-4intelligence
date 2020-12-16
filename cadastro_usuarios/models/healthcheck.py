from typing import List

from pydantic import BaseModel, Field

from cadastro_usuarios.models import parse_openapi


class Healthcheck(BaseModel):
    msg: str = Field(..., description="Estado de saúde da API")


class HealthcheckResponse(BaseModel):
    result: List[Healthcheck] = Field(..., description="Padrão de resposta da API, lista contendo resposta(s)")


HEALTHCHECK_RESPONSE = parse_openapi()
