from cadastro_usuarios.database import DataBase, campos_obrigatorios


class Usuario(DataBase):
    def __init__(self, id_usuario: int = None, nome: str = None, cpf: str = None,
                 data_nascimento: float = None):
        self.__id_usuario = id_usuario
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    def dict(self):
        return {key.replace("_Usuario__", ""): value for key, value in self.__dict__.items() if value}

    @campos_obrigatorios(["nome", "cpf"])
    def inserir(self):
        """
        Insere um usuário no banco de dados.

        :param str nome: Nome do usuário.
        :param str cpf: CPF do usuário, aqui devem ser informados apenas os digítos.
        :return: 1 se o usuário tiver sido inserido, 0 caso contrário.
        :rtype: int
        """
        self.query_string = ""
        if self.__data_nascimento:
            self.query_string = """INSERT INTO USUARIO (NOME, CPF, DATA_NASCIMENTO)
            values (%(nome)s, %(cpf)s, to_timestamp(%(data_nascimento)s, 'YYYY-MM-DD'))"""
        else:
            self.query_string = """INSERT INTO USUARIO (NOME, CPF) values (%(nome)s, %(cpf)s)"""
        return self.insert()

    @campos_obrigatorios(["cpf"])
    def atualizar(self):
        """
        Atualiza um usuário.

        :param str cpf: CPF do usuário.
        :param str nome: Nome do usuário.
        :param str data_nascimento: Data de nascimento do usuário.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = ""
        if self.__data_nascimento:
            self.query_string = "UPDATE USUARIO SET DATA_NASCIMENTO = to_timestamp(%(data_nascimento)s, 'YYYY-MM-DD')"
        if self.__nome:
            self.query_string = "UPDATE USUARIO SET NOME = %(nome)s"
        if self.__data_nascimento and self.__nome:
            self.query_string = """UPDATE USUARIO SET DATA_NASCIMENTO = to_timestamp(%(data_nascimento)s, 'YYYY-MM-DD'),
                                NOME = %(nome)s"""
        self.query_string += " WHERE USUARIO.CPF = %(cpf)s"
        return True if self.insert() else False

    @campos_obrigatorios(["cpf"])
    def existe(self):
        """
        Verifica se um usuário existe no banco de dados.

        :param str cpf: CPF do usuário.
        :param str id_usuario: Id do usuário no banco de dados.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = "SELECT COUNT(*) FROM USUARIO WHERE USUARIO.CPF = %(cpf)s"
        if self.__id_usuario:
            self.query_string += " OR USUARIO.ID_USUARIO = %(id_usuario)s"
        return True if self.find_one()[0] else False

    @campos_obrigatorios(["cpf"])
    def deletar(self):
        """
        Deleta um usuário do banco de dados.

        :param str cpf: CPF do usuário.
        :param str id_usuario: Id do usuário no banco de dados.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = "DELETE FROM USUARIO WHERE USUARIO.CPF = %(cpf)s"
        return True if self.insert() else False
