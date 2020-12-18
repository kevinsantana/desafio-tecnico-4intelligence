from typing import Optional

from pydantic import BaseModel, Field


class Paginacao(BaseModel):
    proxima: str = Field(..., description="Proxima página com resultados")
    anterior: str = Field(..., description="Página anterior com resultados")
    primeira: str = Field(..., description="Primeira página que contem resultados")
    ultima: str = Field(..., description="Última página que contem resultados")
    total: int = Field(..., description="Quantidade total de páginas")


class Message(BaseModel):
    status: int = Field(..., description="Código da mensagem")
    mensagem: str = Field(..., description="Detalhes da mensagem")
    stacktrace: Optional[str] = Field("", description="Stacktrace do erro")


DEFAULT_RESPONSES = [
    Message(status=422, mensagem="Os parâmetros da requisição estão inválidos!",
            stacktrace="Traceback (most recent call last): ..."),
    Message(status=500, mensagem="Ocorreu um erro interno!",
            stacktrace="Traceback (most recent call last): ...")
]


def parse_openapi(responses: list = list()) -> dict:
    responses.extend(DEFAULT_RESPONSES)
    return {example.status: {"content": {"application/json": {"example": example.dict()}}, "model": Message}
            for example in responses}
