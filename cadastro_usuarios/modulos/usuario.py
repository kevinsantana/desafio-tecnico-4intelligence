import re

from cadastro_usuarios.database.usuario import Usuario
from cadastro_usuarios.excecoes.usuario import CpfInvalidoException


def __cpf_eh_valido(cpf: str):
    """
    Válida a consistência de um CPF, conforme instruções disponíveis em \
    http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/funcoes.js

    :param str cpf: CPF a se verificar a consistência.
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


def inserir(nome: str, cpf: str, data_nascimento: str = None):
    """
    Insere um usuário no banco de dados, verificando se o cpf é consistente.

    :param str nome: Nome do usuário.
    :param str cpf: CPF do usuário, aqui devem ser informados apenas os digítos.
    :param str data_nascimento: Data de nascimento do usuário.
    :return bool: True se o usuário tiver sido inserido com sucesso, False caso contrário.
    :raises CpfInvalidoException: O CPF informado não é válido.
    """
    cpf = re.sub("[^0-9]", "", cpf)
    cpfs_invalidos = {"00000000000", "11111111111", "22222222222", "33333333333",
                      "44444444444", "55555555555", "66666666666", "77777777777",
                      "88888888888", "99999999999"}
    if cpf in cpfs_invalidos or len(cpf) < 11 or __cpf_eh_valido(cpf) is False:
        raise CpfInvalidoException(416, cpf)
    insercao = Usuario(nome=nome, cpf=cpf, data_nascimento=data_nascimento).inserir()
    return True if insercao else False
