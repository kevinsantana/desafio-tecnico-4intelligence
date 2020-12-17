from cadastro_usuarios.database import DataBase, campos_obrigatorios


class DominioUf(DataBase):
    def __init__(self, id_uf: int = None, uf: str = None, descricao: str = None):
        self.__id_uf = id_uf
        self.__uf = uf
        self.__descricao = descricao

    @property
    def id_uf(self):
        return self.id_uf

    @property
    def uf(self):
        return self.__uf

    @property
    def descricao(self):
        return self.__descricao

    def dict(self):
        return {key.replace("_DominioUf__", ""): value for key, value in self.__dict__.items() if value}

    @campos_obrigatorios(["uf"])
    def buscar_estado(self):
        """
        Retorna o estado da uf.

        :param str uf: Uf do Estado
        :return: Estado que a uf representa.
        :rtype: str
        """
        self.query_string = "SELECT DESCRICAO FROM DOMINIO_UF WHERE DOMINIO_UF.UF = %(uf)s"
        return self.find_one()

    @campos_obrigatorios(["uf"])
    def buscar_id(self):
        """
        Retorna o id da uf.

        :param str uf: Uf do Estado
        :return: Id da uf no banco de dados.
        :rtype: int
        """
        self.query_string = "SELECT ID_UF FROM DOMINIO_UF WHERE DOMINIO_UF.UF = %(uf)s"
        return self.find_one()
