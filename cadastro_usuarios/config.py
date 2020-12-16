import os


PGSQL_DB = os.environ.get("PGSQL_DB", "cadastro_usuarios")
PGSQL_HOST = os.environ.get("PGSQL_HOST", "db_cadastro_usuarios")
PGSQL_PASS = os.environ.get("PGSQL_PASS", "cadastro_usuarios")
PGSQL_USR = os.environ.get("PGSQL_USR", "cadastro_usuarios")
PGSQL_PORT = os.environ.get("PGSQL_PORT", "5432")
