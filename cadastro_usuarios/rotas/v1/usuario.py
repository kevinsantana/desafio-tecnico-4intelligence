from fastapi import APIRouter, Body

from cadastro_usuarios.modulos import usuario as usr
from cadastro_usuarios.modelos.usuario import (
    InserirUsuarioResponse, USER_INSERT_DEFAULT_RESPONSE, Usuario
    )

router = APIRouter()


@router.post("/", status_code=200, summary="Insere um usuário", response_model=InserirUsuarioResponse,
             responses=USER_INSERT_DEFAULT_RESPONSE)
async def inserir(
    dados_usuario: Usuario = Body(
        ...,
        example={
            "nome": "Jose da Silva",
            "cpf": "12345678912",
            "data_nascimento": "2016-06-22 19:10:25-07"
        }
    )
):
    """
    Endpoint para efetuar a gravação de um usuário no banco de dados de forma assíncrona
    """
    return {"resultado": [usr.inserir(**dados_usuario.dict())]}
