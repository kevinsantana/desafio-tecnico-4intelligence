from typing import List, Optional
from pydantic import BaseModel, Field

from cadastro_usuarios.modelos import Message, parse_openapi


class Usuario(BaseModel):
    nome: str = Field(..., description="Nome do usuário")
    cpf: str = Field(..., description="CPF do usuário")
    data_nascimento: Optional[str] = Field(description="Data de aniversário do usuário")


class InserirUsuarioResponse(BaseModel):
    resultado: List[bool] = Field(..., description="Id do usuário cadastrado")


USER_INSERT_DEFAULT_RESPONSE = parse_openapi([
    Message(status=400, mensagem="O cpf já foi cadastrado",
            stacktrace="Traceback (most recent call last): ..."),
    Message(status=416, mensagem="O cpf é inválido",
            stacktrace="Traceback (most recent call last): ...")
])
