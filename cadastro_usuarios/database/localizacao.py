from cadastro_usuarios.database import DataBase, campos_obrigatorios


class Localizacao(DataBase):
    def __init__(self, id_localizacao: int = None, rua: str = None, numero: int = None,
                 cep: str = None, cidade: str = None, bairro: str = None):
        self.__id_localizacao = id_localizacao
        self.__rua = rua
        self.__numero = numero
        self.__cep = cep
        self.__cidade = cidade
        self.__bairro = bairro

    @property
    def id_localizacao(self):
        return self.__id_localizacao

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

    def dict(self):
        return {key.replace("_Localizacao__", ""): value for key, value in self.__dict__.items() if value}

    @campos_obrigatorios(["rua", "cep", "cidade", "bairro"])
    def inserir(self):
        """
        Insere uma localização no banco dados. O endereço foi desmembrado em outras \
        duas tabelas para que fosse possível associar mais de um endereço ao usuário \
        e permitir que um mesmo nome de rua, cidade ou até bairro exista em mais de uma \
        uf.

        :param str rua: Rua da localização.
        :param str cep: Cep da localização.
        :param str cidade: Cidade da localização.
        :param str bairro: Bairro da localização.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = ""
        if self.__numero:
            self.query_string = """INSERT INTO LOCALIZACAO (rua, numero, cep, cidade, bairro)
                                values (%(rua)s, %(numero)s, %(cep)s, %(cidade)s, %(bairro)s)"""
        else:
            self.query_string = """INSERT INTO LOCALIZACAO (rua, cep, cidade, bairro)
                                values (%(rua)s, %(cep)s, %(cidade)s, %(bairro)s)"""
        return True if self.insert() else False

    @campos_obrigatorios(["cep", "rua", "bairro", "cidade"])
    def buscar_id(self):
        """
        Retorna o id da uf.

        :param str uf: Uf do Estado
        :return: Id da uf no banco de dados.
        :rtype: int
        """
        self.query_string = """SELECT ID_LOCALIZACAO FROM LOCALIZACAO WHERE LOCALIZACAO.CEP = %(cep)s
                            AND LOCALIZACAO.CIDADE = %(cidade)s AND LOCALIZACAO.BAIRRO = %(bairro)s
                            AND LOCALIZACAO.RUA = %(rua)s"""
        return self.find_one()

    @campos_obrigatorios(["id_localizacao"])
    def atualizar(self, dados_atualizacao: dict):
        """
        Atualiza a localização de um usuário. Para permitir a atualização genérica, ou seja, \
        para que seja possível atualizar um campo qualquer (com exceção da uf e do estado) da \
        localização de um usuário, foi preciso iterar sobre as informaçõesa serem atualizadas \
        e montando a consulta. As últimas linhas trata da retirada do caracter ',' da clásula \
        de atualização, i.e, ', WHERE LOCALIZACAO...'

        :param str id_localizacao: Id da localização associada ao usuário.
        :param dict dados_atualizacao: Dados da atualização.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = "UPDATE LOCALIZACAO SET"
        for coluna, valor in list(dados_atualizacao.items())[:-1]:
            self.query_string += f" {coluna.upper()} = '{valor}',"
        self.query_string += " WHERE LOCALIZACAO.ID_LOCALIZACAO = %(id_localizacao)s"
        ultima_virgula = self.query_string.rfind(",")
        self.query_string = self.query_string[:ultima_virgula] + "" + self.query_string[ultima_virgula+1:]
        return True if self.insert() else False
