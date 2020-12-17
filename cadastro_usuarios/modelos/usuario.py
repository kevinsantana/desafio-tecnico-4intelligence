from typing import List, Optional
from pydantic import BaseModel, Field

from cadastro_usuarios.modelos import Message, parse_openapi


class Usuario(BaseModel):
    nome: str = Field(..., description="Nome do usuário")
    cpf: str = Field(..., description="CPF do usuário")
    data_nascimento: Optional[str] = Field(description="Data de aniversário do usuário")


class InserirUsuarioResponse(BaseModel):
    resultado: List[bool] = Field(..., description="Indicação se o usuário foi ou não criado")


class AtualizarUsuarioRequest(BaseModel):
    nome: Optional[str] = Field(description="Nome do usuário")
    data_nascimento: Optional[str] = Field(description="Data de aniversário do usuário")


class AtualizarUsuarioResponse(BaseModel):
    resultado: List[bool] = Field(..., description="Indicação se o usuário foi ou não atualizado")


class DeletarUsuarioResponse(BaseModel):
    resultado: List[bool] = Field(..., description="Indicação se a operação foi executada ou não")


USER_INSERT_DEFAULT_RESPONSE = parse_openapi([
    Message(status=400, mensagem="O cpf já foi cadastrado",
            stacktrace="Traceback (most recent call last): ..."),
    Message(status=416, mensagem="O cpf é inválido",
            stacktrace="Traceback (most recent call last): ..."),
    Message(status=404, mensagem="O usuário não existe",
            stacktrace="Traceback (most recent call last): ...")
])
USER_UPDATE_DEFAULT_RESPONSE = parse_openapi([
    Message(status=404, mensagem="O usuário não existe",
            stacktrace="Traceback (most recent call last): ..."),
    Message(status=403, mensagem="É preciso informar ao menos um campo",
            stacktrace="Traceback (most recent call last): ...")
])
USER_DELETE_DEFAULT_RESPONSE = parse_openapi([
    Message(status=404, mensagem="O usuário não existe",
            stacktrace="Traceback (most recent call last): ...")
])
