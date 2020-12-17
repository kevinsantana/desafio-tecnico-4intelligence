import re
import functools

import requests
from loguru import logger

from cadastro_usuarios.database.uf import DominioUf
from cadastro_usuarios.database.usuario import Usuario
from cadastro_usuarios.database.endereco import Endereco
from cadastro_usuarios.modulos.usuario import _limpa_cpf
from cadastro_usuarios.database.localizacao import Localizacao
from cadastro_usuarios.database.local_publico import LocalPublico
from cadastro_usuarios.excecoes.endereco import CepInvalidoException, ServicoException


def __limpa_cep(cep):
    def decorator_limpa_cep(func):
        @functools.wraps(func)
        def wrapper_limpa_cep(*args, **kwargs):
            kwargs["cep"] = re.sub("[^0-9]", "", kwargs["cep"])
            return func(*args, **kwargs)
        return wrapper_limpa_cep
    return decorator_limpa_cep


def __montar_endereco(endereco: dict):
    estado = DominioUf(uf=endereco.get("uf")).buscar_estado().get("descricao")
    return {
        "cep": endereco.get("cep"),
        "rua": endereco.get("logradouro"),
        "bairro": endereco.get("bairro"),
        "cidade": endereco.get("localidade"),
        "uf": endereco.get("uf").upper(),
        "estado": estado.title()
    }


@__limpa_cep("cep")
def validar_cep(*, cep: str):
    """
    Consulta se o cep é válido e retorna as suas informações. A consulta é feita \
    através de uma requisição fora do projeto.

    :param str cep: Cep buscado.
    :return: Dados da localização do CEP, caso seja válido
    :rtype: dict
    :raises CepInvalidoException: Se o CEP for inválido
    :raises ServicoException: Se o serviço consumido para consulta esteja indisponível \
    ou, ainda, não for possível efetuar uma requisição.
    """
    url_validar_cep = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        requisicao_verificar_cep = requests.get(url=url_validar_cep)
        if requisicao_verificar_cep.status_code != 200 or requisicao_verificar_cep.json().get("erro") is True:
            raise CepInvalidoException(404, cep)
        else:
            resposta = __montar_endereco(requisicao_verificar_cep.json())
            logger.debug(resposta)
            return __montar_endereco(requisicao_verificar_cep.json())
    except requests.exceptions.ConnectionError as connection_error:
        raise ServicoException(500, connection_error)


@__limpa_cep("cep")
@_limpa_cpf("cpf")
def inserir(*, cpf: str, cep: str, rua: str, bairro: str, cidade: str, uf: str,
            estado: str, numero: int = None, id_usuario: int = None):
    """
    Insere o endereço de um usuário no banco de dados. O endereço foi desmembrado \
    em outras tabelas para que fosse possível cadastrar mais de um endereço para um \
    usuário (histórico de mudanças), associar um mesmo endereço a usuários diferentes \
    (usuários que residem na mesma casa) e rua, bairro e cidades que compartilham o mesmo \
    nome em UFs diferentes.

    :param str cpf: CPF do usuário.
    :param cep: CEP da residência do usuário.
    :param rua: Rua do usuário.
    :param bairro: Bairro do usuário.
    :param str cidade: Cidade do usuário.
    :param str uf: UF do endereço do usuário.
    :param str estado: Estado do usuário.
    :param int numero: Número da casa/apartamento do usuário. Nulo permitindo os \
    casos em que uma residência não possuí número, i.e, sem número (s/n).
    :param int id_usuario: Alternantiva ao CPF do usuário, para cadastro do endereço.
    :return: True se o endereço for associado ao usuário, False caso contrário.
    :rtype: bool
    """
    id_uf = DominioUf(uf=uf).buscar_id().get("id_uf")
    id_usuario = id_usuario if id_usuario else Usuario(cpf=cpf).buscar_id().get("id_usuario")
    localizacao = Localizacao(cep=cep, rua=rua, bairro=bairro, cidade=cidade, numero=numero)
    if localizacao.inserir():
        id_localizacao = localizacao.buscar_id().get("id_localizacao")
        LocalPublico(id_uf=id_uf, id_localizacao=id_localizacao).inserir()
    endereco = Endereco(id_uf=id_uf, id_localizacao=id_localizacao, id_usuario=id_usuario)
    if endereco.inserir():
        return True
    else:
        return False
