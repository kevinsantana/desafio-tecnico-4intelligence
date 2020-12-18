from fastapi import APIRouter, Query, Body

from cadastro_usuarios.modulos import endereco as edr
from cadastro_usuarios.modelos.endereco import (
    BuscarCepResponse, BUSCAR_ENDERECO_DEFAULT_RESPONSE, InserirEnderecoResquest, InserirEnderecoResponse,
    INSERIR_ENDERECO_DEFAULT_RESPONSE, AtualizarEnderecoRequest, AtualizarEnderecoResponse,
    ATUALIZAR_ENDERECO_DEFAULT_RESPONSE, DeletarEnderecoResponse, DELETAR_ENDERECO_DEFAULT_RESPONSE
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
            "cpf": "48157396840",
            "cep": "13083-970",
            "rua": "Rua Carlos Gomes",
            "numero": 77,
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


@router.put("/{cpf}/{id_endereco}", status_code=200, summary="Atualizar o endereço de um usuário",
            response_model=AtualizarEnderecoResponse, responses=ATUALIZAR_ENDERECO_DEFAULT_RESPONSE)
def atualizar(cpf: str = Query(..., description="CPF do usuário"),
              id_endereco: str = Query(..., description="Endereço associado ao usuário"),
              dados_atualizacao: AtualizarEnderecoRequest = Body(..., description="Dados relativos a atualização")):
    """
    Atualiza o endereço de um usuário.
    """
    return {"resultado": [edr.atualizar(cpf=cpf, id_endereco=id_endereco, dados_atualizacao=dados_atualizacao.dict())]}


@router.delete("/{cpf}/{id_endereco}", status_code=200, summary="Deleta um endereço associado a um usuário",
               response_model=DeletarEnderecoResponse, responses=DELETAR_ENDERECO_DEFAULT_RESPONSE)
def deletar(cpf: str = Query(..., description="CPF do usuário"),
            id_endereco: str = Query(..., description="Endereço associado ao usuário")):
    return {"resultado": [edr.deletar(cpf=cpf, id_endereco=id_endereco)]}
