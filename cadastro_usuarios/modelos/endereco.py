from typing import List, Optional
from pydantic import BaseModel, Field

from cadastro_usuarios.modelos import Message, parse_openapi


class Endereco(BaseModel):
    cep: str = Field(..., description="CEP do endereço")
    rua: str = Field(..., description="Rua do endereço")
    numero: Optional[str] = Field(description="Número da casa/apartamento")
    bairro: str = Field(description="Bairro do endereço")
    cidade: str = Field(description="Cidade do endereço")
    uf: str = Field(description="uf do endereço")
    estado: str = Field(description="Estado do endereço")


class BuscarCepResponse(BaseModel):
    resultado: List[Endereco] = Field(..., description="Dados do cep buscado")


class InserirEnderecoResquest(Endereco):
    cpf: str = Field(..., description="CPF do usuário")


class InserirEnderecoResponse(BaseModel):
    resultado: List[bool] = Field(..., description="Informa se o endereço foi ou não inserido")


class AtualizarEnderecoRequest(BaseModel):
    cep: Optional[str] = Field(description="CEP do endereço")
    rua: Optional[str] = Field(description="Rua do endereço")
    numero: Optional[str] = Field(description="Número da casa/apartamento")
    bairro: Optional[str] = Field(description="Bairro do endereço")
    cidade: Optional[str] = Field(description="Cidade do endereço")


class AtualizarEnderecoResponse(BaseModel):
    resultado: List[bool] = Field(..., description="Informa se o endereço foi ou não atualizado")


class DeletarEnderecoResponse(BaseModel):
    resultado: List[bool] = Field(..., description="Informa se o endereço foi ou não deletado")


BUSCAR_ENDERECO_DEFAULT_RESPONSE = parse_openapi([
    Message(status=404, mensagem="O cep informado é inválido",
            stacktrace="Traceback (most recent call last): ..."),
    Message(status=500, mensagem="Não foi possível válidar o cep, devido a falha de conectividade",
            stacktrace="Traceback (most recent call last): ...")
])
INSERIR_ENDERECO_DEFAULT_RESPONSE = parse_openapi()
ATUALIZAR_ENDERECO_DEFAULT_RESPONSE = parse_openapi([
    Message(status=416, mensagem="Nenhum dado foi fornecido para alteração",
            stacktrace="Traceback (most recent call last): ..."),
    Message(status=404, mensagem="O usuário não existe",
            stacktrace="Traceback (most recent call last): ...")
])
DELETAR_ENDERECO_DEFAULT_RESPONSE = parse_openapi([
    Message(status=404, mensagem="O usuário não existe",
            stacktrace="Traceback (most recent call last): ...")
])
