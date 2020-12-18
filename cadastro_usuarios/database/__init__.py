import abc
import functools

import psycopg2
from loguru import logger
from psycopg2.extras import DictCursor
from psycopg2 import OperationalError

from cadastro_usuarios.excecoes import CamposObrigatoriosException
from cadastro_usuarios.config import (
    PGSQL_DB, PGSQL_HOST, PGSQL_PASS, PGSQL_PORT, PGSQL_USR,
)


def campos_obrigatorios(campos):
    def decorator_campos_obrigatorios(func):
        @functools.wraps(func)
        def wrapper_campos_obrigatorios(self, *args, **kwargs):
            for campo in campos:
                if self.dict().get(campo) is None:
                    raise CamposObrigatoriosException(self.__class__.__name__, campo)
            return func(self, *args, **kwargs)
        return wrapper_campos_obrigatorios
    return decorator_campos_obrigatorios


class DataBase():
    def __connect(self):
        while True:
            try:
                self.__connection = psycopg2.connect(user=PGSQL_USR,
                                                     password=PGSQL_PASS,
                                                     host=PGSQL_HOST,
                                                     port=PGSQL_PORT,
                                                     database=PGSQL_DB)
                if self.__connection:
                    self.__cursor = self.__connection.cursor(cursor_factory=DictCursor)
                    break
            except OperationalError:
                logger.info("Falha na conexão com o o banco de dados")
                continue

    def __disconect(self):
        self.__cursor.close()
        self.__connection.close()

    def insert(self):
        self.__connect()
        self.__cursor.execute(self.query_string, self.dict())
        self.__connection.commit()
        result = self.__cursor.rowcount
        self.__disconect()
        return result

    def find_one(self):
        self.__connect()
        self.__cursor.execute(self.query_string, self.dict())
        result = self.__cursor.fetchone()
        self.__disconect()
        return result

    def find_all(self, total=False):
        self.__connect()
        self.__cursor.execute(self.query_string, self.dict())
        result = self.__cursor.fetchall()
        self.__disconect()
        if total:
            return result, self.__cursor.rowcount
        return result

    @abc.abstractclassmethod
    def dict(self):
        raise NotImplementedError
