from cadastro_usuarios.excecoes import CadastroUsuarioException


class CpfInvalidoException(CadastroUsuarioException):
    def __init__(self, status_code: int, cpf: str):
        self.status_code = status_code
        self.mensagem = f"O cpf {cpf} é inválido"
        super().__init__(self.status_code, self.mensagem)


class UsuarioJaCadastradoException(CadastroUsuarioException):
    def __init__(self, status_code: int, cpf: str):
        self.status_code = status_code
        self.mensagem = f"O cpf {cpf} já foi registrado"
        super().__init__(self.status_code, self.mensagem)


class UsuarioInexistenteException(CadastroUsuarioException):
    def __init__(self, status_code: int, id_usuario: int = None, cpf: str = None):
        self.status_code = status_code
        self.message = f"O id {id_usuario} do usuário não existe" if id_usuario else f"O cpf {cpf} não existe"
        super().__init__(self.status_code, self.message)


class FiltroException(CadastroUsuarioException):
    def __init__(self, status_code: int):
        self.status_code = status_code
        self.message = "É preciso informar ao menos um campo"
        super().__init__(self.status_code, self.message)
