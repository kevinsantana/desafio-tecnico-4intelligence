import re
import functools

from cadastro_usuarios.database.usuario import Usuario, ListarUsuario
from cadastro_usuarios.excecoes.usuario import (
    CpfInvalidoException, UsuarioJaCadastradoException, UsuarioInexistenteException,
    FiltroException
    )


def _limpa_cpf(cpf):
    def decorator_limpa_cpf(func):
        @functools.wraps(func)
        def wrapper_limpa_cpf(*args, **kwargs):
            kwargs["cpf"] = re.sub("[^0-9]", "", kwargs["cpf"])
            return func(*args, **kwargs)
        return wrapper_limpa_cpf
    return decorator_limpa_cpf


def __montar_usuarios(usuarios: dict):
    return [{
        "nome": usuario.nome,
        "cpf": usuario.cpf,
        "data_nascimento": str(usuario.data_nascimento) if usuario.data_nascimento else usuario.data_nascimento,
        "cep": usuario.cep,
        "rua": usuario.rua,
        "numero": usuario.numero,
        "bairro": usuario.bairro,
        "cidade": usuario.cidade,
        "uf": usuario.uf,
        "estado": usuario.estado
    } for usuario in usuarios]


def __cpf_eh_valido(*, cpf: str):
    """
    Válida a consistência de um CPF, conforme instruções disponíveis em \
    http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/funcoes.js

    :param str cpf: CPF a se verificar a consistência.
    :return: True se o CPF for consistente, isto é, segue as regras do Ministério \
    da Fazenda para composição de um CPF.
    :rtype: bool
    """
    digitos_cpf, digito_verificador1, digito_verificador2 = list(map(int, cpf[:9])), int(cpf[9]), int(cpf[10])
    resultado_primeiro_digito = sum(map(lambda x: x[0]*x[1], zip(range(1, 10), digitos_cpf))) % 11
    primeiro_digito_verificador = resultado_primeiro_digito if resultado_primeiro_digito != 10 else 0
    if primeiro_digito_verificador != digito_verificador1:
        return False
    digitos_cpf.append(primeiro_digito_verificador)
    resultado_segundo_digito = sum(map(lambda x: x[0]*x[1], zip(range(10), digitos_cpf))) % 11
    segundo_digito_verificador = resultado_segundo_digito if resultado_segundo_digito != 10 else 0
    return True if segundo_digito_verificador == digito_verificador2 else False


@_limpa_cpf("cpf")
def inserir(*, nome: str, cpf: str, data_nascimento: str = None):
    """
    Insere um usuário no banco de dados, verificando se o cpf é consistente.

    :param str nome: Nome do usuário.
    :param str cpf: CPF do usuário, aqui devem ser informados apenas os digítos.
    :param str data_nascimento: Data de nascimento do usuário.
    :return: True se o usuário tiver sido inserido com sucesso, False caso contrário.
    :rtype: bool
    :raises CpfInvalidoException: O CPF informado não é válido.
    """
    if Usuario(cpf=cpf).existe():
        raise UsuarioJaCadastradoException(403, cpf)
    cpfs_invalidos = {"00000000000", "11111111111", "22222222222", "33333333333",
                      "44444444444", "55555555555", "66666666666", "77777777777",
                      "88888888888", "99999999999"}
    if cpf in cpfs_invalidos or len(cpf) != 11 or __cpf_eh_valido(cpf=cpf) is False:
        raise CpfInvalidoException(416, cpf)
    insercao = Usuario(nome=nome, cpf=cpf, data_nascimento=data_nascimento).inserir()
    return True if insercao else False


@_limpa_cpf("cpf")
def atualizar(*, cpf: str, data_nascimento: str = None, nome: str = None):
    """
    Efetua a atulização no banco de dados referentes as informações do usuário.

    :param str cpf: CPF do usuário
    :param str data_nascimento: Data de nascimento do usuário, em formato timestamp.
    :param str nome: Nome do usuário
    :return: True se o usuário tiver sido atualizado com sucesso, False caso contrário.
    :rtype: bool
    :raises FiltroException: Se nenhum campo for informado para a atualização
    :raises UsuarioInexistenteException: Caso o usuário informado não exista no banco de dados.
    """
    if Usuario(cpf=cpf).existe():
        return Usuario(cpf=cpf, data_nascimento=data_nascimento).atualizar()
    elif not data_nascimento and not nome:
        raise FiltroException(403)
    else:
        raise UsuarioInexistenteException(404, cpf)


@_limpa_cpf("cpf")
def deletar(*, cpf: str):
    """
    Excluí um usuário do banco de dados.

    :param str cpf: CPF do usuário
    :return: True se a operação for executada com sucesso, False caso contrário.
    :rtype: bool
    :raises UsuarioInexistenteException: Caso o usuário informado não exista no banco de dados.
    """
    if Usuario(cpf=cpf).existe():
        return Usuario(cpf=cpf).deletar()
    else:
        raise UsuarioInexistenteException(404, cpf)


@_limpa_cpf("cpf")
def listar_um(*, cpf: str):
    """
    Lista as informações de um usuário no banco de dados.

    :param str cpf: CPF do usuário buscado.
    :return: Informações do usuário buscado.
    :rtype: dict
    :raises UsuarioInexistenteException: Caso o usuário informado não exista no banco de dados.
    """
    if Usuario(cpf=cpf).existe():
        usuario = ListarUsuario(cpf=cpf).listar_um()
        usuario.data_nascimento = str(usuario.data_nascimento) if usuario.data_nascimento else usuario.data_nascimento
        return usuario.dict()
    else:
        raise UsuarioInexistenteException(404, cpf)


def listar_todos(quantidade: int, pagina: int):
    """
    Lista as informações de um usuário.
    :param int pagina: Offset da página.
    :param int quantidade: Quantidade de usuários pra listar.
    :return: Total de usuários e usuários da base.
    :rtype: int, list
    """
    total, usuarios = ListarUsuario().listar_todos(quantidade=quantidade, pagina=pagina)
    return total, __montar_usuarios(usuarios)
