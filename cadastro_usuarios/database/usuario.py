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
            values (%(nome)s, %(cpf)s, to_timestamp(%(data_nascimento)s)) RETURNING id_usuario"""
        else:
            self.query_string = """INSERT INTO USUARIO (NOME, CPF) values (%(nome)s, %(cpf)s)"""
        return self.insert()
