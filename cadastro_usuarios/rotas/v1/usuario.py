from fastapi import APIRouter, Body, Query

from cadastro_usuarios.modulos import usuario as usr
from cadastro_usuarios.modelos.usuario import (
    InserirUsuarioResponse, USER_INSERT_DEFAULT_RESPONSE, Usuario, AtualizarUsuarioResponse,
    USER_UPDATE_DEFAULT_RESPONSE, AtualizarUsuarioRequest, DeletarUsuarioResponse,
    USER_DELETE_DEFAULT_RESPONSE, ListarUsuarioResponse, LISTAR_UM_USUARIO_DEFAULT_RESPONSE
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


@router.put("/{cpf}", status_code=200, summary="Atualizar um usuário", response_model=AtualizarUsuarioResponse,
            responses=USER_UPDATE_DEFAULT_RESPONSE)
def atualizar(cpf: str = Query(..., description="CPF do usuário"),
              dados_atualizacao: AtualizarUsuarioRequest = Body(..., description="Dados relativos a atualização")):
    """
    Atualiza um usuário
    """
    return {"resultado": [usr.atualizar(cpf=cpf, **dados_atualizacao.dict())]}


@router.delete("/{cpf}", status_code=200, summary="Deleta um usuário",
               response_model=DeletarUsuarioResponse, responses=USER_DELETE_DEFAULT_RESPONSE)
def deletar(cpf: str = Query(..., description="CPF do usuário")):
    return {"resultado": [usr.deletar(cpf=cpf)]}


@router.get("/{cpf}", status_code=200, summary="Listar as informações de um usuário",
            response_model=ListarUsuarioResponse, responses=LISTAR_UM_USUARIO_DEFAULT_RESPONSE)
def listar_um(cpf: str = Query(..., description="CPF do usuário")):
    """
    Lista um usuário
    """
    return {"resultado": [usr.listar_um(cpf=cpf)]}
