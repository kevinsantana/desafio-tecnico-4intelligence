from fastapi import APIRouter, Query, Body

from cadastro_usuarios.modulos import endereco as edr
from cadastro_usuarios.modelos.endereco import (
    BuscarCepResponse, BUSCAR_ENDERECO_DEFAULT_RESPONSE, InserirEnderecoResquest, InserirEnderecoResponse,
    INSERIR_ENDERECO_DEFAULT_RESPONSE
    )


router = APIRouter()


@router.get("/{cep}", status_code=200, summary="Busca o endereço a partir do cep",
            response_model=BuscarCepResponse, responses=BUSCAR_ENDERECO_DEFAULT_RESPONSE)
def buscar_endereco(cep: str = Query(..., description="cep buscado")):
    """
    Endpoint para válidar um cep e retornar seu resultado.
    """
    return {"resultado": [edr.validar_cep(cep=cep)]}


@router.post("/", status_code=200, summary="Insere um endereço", response_model=InserirEnderecoResponse,
             responses=INSERIR_ENDERECO_DEFAULT_RESPONSE)
def inserir(
    dados_endereco: InserirEnderecoResquest = Body(
        ...,
        example={
            "cpf": "12345678912",
            "cep": "13083-970",
            "rua": "Rua Carlos Gomes 241",
            "bairro": "Cidade Universitária",
            "cidade": "Campinas",
            "uf": "SP",
            "estado": "São Paulo"
        }
    )
):
    """
    Endpoint para efetuar a gravação de um usuário no banco de dados de forma assíncrona
    """
    return {"resultado": [edr.inserir(**dados_endereco.dict())]}
