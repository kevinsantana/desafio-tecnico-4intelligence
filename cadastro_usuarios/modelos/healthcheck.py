from typing import List

from pydantic import BaseModel, Field

from cadastro_usuarios.modelos import parse_openapi


class Healthcheck(BaseModel):
    msg: str = Field(..., description="Estado de saúde da API")


class HealthcheckResponse(BaseModel):
    resultado: List[Healthcheck] = Field(..., description="Padrão de resposta da API, lista contendo resposta(s)")


HEALTHCHECK_RESPONSE = parse_openapi()
