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
