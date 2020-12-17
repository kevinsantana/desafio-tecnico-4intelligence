from cadastro_usuarios.database import DataBase, campos_obrigatorios


class Usuario(DataBase):
    def __init__(self, id_usuario: int = None, nome: str = None, cpf: str = None,
                 data_nascimento: float = None):
        self.__id_usuario = id_usuario
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    @property
    def id_usuario(self):
        return self.__id_usuario

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
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = ""
        if self.__data_nascimento:
            self.query_string = """INSERT INTO USUARIO (NOME, CPF, DATA_NASCIMENTO)
            values (%(nome)s, %(cpf)s, to_timestamp(%(data_nascimento)s, 'YYYY-MM-DD'))"""
        else:
            self.query_string = """INSERT INTO USUARIO (NOME, CPF) values (%(nome)s, %(cpf)s)"""
        return True if self.insert() else False

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

    @campos_obrigatorios(["cpf"])
    def buscar_id(self):
        """
        Busca o id do usuário no banco de dados a partir do cpf.

        :param str cpf: CPF do usuário.
        :return: Id do usuário.
        :rtype: dict
        """
        self.query_string = "SELECT ID_USUARIO FROM USUARIO WHERE USUARIO.CPF = %(cpf)s"
        return self.find_one()


class ListarUsuario(DataBase):
    def __init__(self, nome: str = None, cpf: str = None, data_nascimento: float = None,
                 rua: str = None, numero: int = None, cep: str = None, cidade: str = None,
                 bairro: str = None, uf: str = None, descricao: str = None):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__rua = rua
        self.__numero = numero
        self.__cep = cep
        self.__cidade = cidade
        self.__bairro = bairro
        self.__uf = uf
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return str(self.__data_nascimento) if self.__data_nascimento else self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = str(data_nascimento)

    @property
    def rua(self):
        return self.__rua

    @property
    def numero(self):
        return self.__numero

    @property
    def cep(self):
        return self.__cep

    @property
    def cidade(self):
        return self.__cidade

    @property
    def bairro(self):
        return self.__bairro

    @property
    def uf(self):
        return self.__uf

    @property
    def descricao(self):
        return self.__descricao

    def dict(self):
        return {key.replace("_ListarUsuario__", ""): value for key, value in self.__dict__.items()}

    @campos_obrigatorios(["cpf"])
    def listar_um(self):
        """
        Lista as informações de um usuário.

        :param str cpf: CPF do usuário.
        :return: Informações do usuário buscado.
        :rtype: ListarUsuario
        """
        self.query_string = """SELECT NOME, CPF, DATA_NASCIMENTO, RUA, NUMERO, CEP, CIDADE, BAIRRO, UF, DESCRICAO
                            FROM USUARIO
                            JOIN ENDERECO ON ENDERECO.ID_USUARIO = USUARIO.ID_USUARIO
                            JOIN LOCAL_PUBLICO ON LOCAL_PUBLICO.ID_UF = ENDERECO.ID_UF
                            JOIN LOCALIZACAO ON LOCALIZACAO.ID_LOCALIZACAO = LOCAL_PUBLICO.ID_LOCALIZACAO
                            JOIN DOMINIO_UF ON DOMINIO_UF.ID_UF = LOCAL_PUBLICO.ID_UF
                            WHERE USUARIO.CPF = %(cpf)s"""
        usuario = self.find_one()
        return ListarUsuario(**dict(usuario)) if usuario else None
