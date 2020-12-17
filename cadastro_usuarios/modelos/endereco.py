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
    descricao: str = Field(description="Estado do endereço")


class BuscarCepResponse(BaseModel):
    resultado: List[Endereco] = Field(..., description="Dados do cep buscado")


class InserirEnderecoResquest(Endereco):
    cpf: str = Field(..., description="CPF do usuário")


class InserirEnderecoResponse(BaseModel):
    resultado: List[bool] = Field(..., description="Dados do cep buscado")


BUSCAR_ENDERECO_DEFAULT_RESPONSE = parse_openapi([
    Message(status=404, mensagem="O cep informado é inválido",
            stacktrace="Traceback (most recent call last): ..."),
    Message(status=500, mensagem="Não foi possível válidar o cep, devido a falha de conectividade",
            stacktrace="Traceback (most recent call last): ...")
])
INSERIR_ENDERECO_DEFAULT_RESPONSE = parse_openapi()
