from cadastro_usuarios.database import DataBase, campos_obrigatorios


class Endereco(DataBase):
    def __init__(self, id_endereco: int = None, id_uf: int = None, id_localizacao: int = None,
                 id_usuario: str = None):
        self.__id_endereco = id_endereco
        self.__id_uf = id_uf
        self.__id_localizacao = id_localizacao
        self.__id_usuario = id_usuario

    @property
    def id_endereco(self):
        return self.__id_endereco

    @property
    def id_uf(self):
        return self.__id_uf

    @property
    def id_localizacao(self):
        return self.__id_localizacao

    @property
    def id_usuario(self):
        return self.__id_usuario

    def dict(self):
        return {key.replace("_Endereco__", ""): value for key, value in self.__dict__.items()}

    @campos_obrigatorios(["id_uf", "id_localizacao", "id_usuario"])
    def inserir(self):
        """
        Insere um endereço no banco de dados. A associação de usuário, uf e local \
        público qualifica um endereço, assim, permitindo a inserção de mais de\
        um local para um mesmo usuário e um mesmo endereço para usuário diferentes \
        (caso em que dois usuários residem no mesmo endereço).

        :param str id_uf: Id da uf no banco de dados.
        :param str id_localizacao: Id da localização no banco de dados.
        :param str id_usuario: Id do usuário no banco de dados.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = """INSERT INTO ENDERECO (id_uf, id_localizacao, id_usuario)
                            values (%(id_uf)s, %(id_localizacao)s, %(id_usuario)s)"""
        return True if self.insert() else False

    @campos_obrigatorios(["id_uf", "id_localizacao", "id_usuario"])
    def esta_associado(self):
        """
        Verifica se a localização está associada ao usuário, ou seja, se é um \
        endereço associado do usuário.

        :param str id_uf: Id da uf no banco de dados.
        :param str id_localizacao: Id da localização no banco de dados.
        :param str id_usuario: Id do usuário no banco de dados.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = """SELECT COUNT(*) FROM ENDERECO WHERE ENDERECO.ID_UF = %(id_uf)s AND
                            ENDERECO.ID_LOCALIZACAO = %(id_localizacao)s AND ENDERECO.ID_USUARIO = %(id_usuario)s"""
        return True if self.find_one()[0] else False

    @campos_obrigatorios(["id_endereco"])
    def buscar(self):
        """
        Retorna as informações associadas ao endereco.

        :param str id_endereco: Id do endereço que deseja-se checar a associação.
        :return: id_uf, id_localizacao e id_usuario associados ao endereço.
        :rtype: DictRow
        """
        self.query_string = """SELECT ID_UF, ID_LOCALIZACAO, ID_USUARIO FROM ENDERECO
                            WHERE ENDERECO.ID_ENDERECO = %(id_endereco)s"""
        return self.find_one()

    @campos_obrigatorios(["id_endereco"])
    def deletar(self):
        """
        Deleta um endereço associado a um usuário do banco de dados. Não há delete \
        on cascade, pois, o endereço é associado a um usuário, enquanto a localização \
        pode ser associada a um ou vários usuários.

        :param str id_endereco: Id do endereço asssociada ao usuário.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = "DELETE FROM ENDERECO WHERE ENDERECO.ID_ENDERECO = %(id_endereco)s"
        return True if self.insert() else False
