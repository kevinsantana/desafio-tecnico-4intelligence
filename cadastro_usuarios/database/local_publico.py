from cadastro_usuarios.database import DataBase, campos_obrigatorios


class LocalPublico(DataBase):
    def __init__(self, id_uf: int = None, id_localizacao: int = None):
        self.__id_uf = id_uf
        self.__id_localizacao = id_localizacao

    @property
    def id_uf(self):
        return self.__id_uf

    @property
    def id_localizacao(self):
        return self.__id_localizacao

    def dict(self):
        return {key.replace("_LocalPublico__", ""): value for key, value in self.__dict__.items() if value}

    @campos_obrigatorios(["id_uf", "id_localizacao"])
    def inserir(self):
        """
        Insere um local público no banco dados.

        :param str id_uf: Id da Uf.
        :param str id_localizacao: Id da localização.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = "INSERT INTO LOCAL_PUBLICO (id_uf, id_localizacao) values (%(id_uf)s, %(id_localizacao)s)"
        return True if self.insert() else False
