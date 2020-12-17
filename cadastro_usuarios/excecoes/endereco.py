from cadastro_usuarios.excecoes import CadastroUsuarioException


class CepInvalidoException(CadastroUsuarioException):
    def __init__(self, status_code: int, cep: str):
        self.status_code = status_code
        self.mensagem = f"O cep {cep} informado é inválido"
        super().__init__(self.status_code, self.mensagem)


class ServicoException(CadastroUsuarioException):
    def __init__(self,  status_code: str, retorno_servico: str):
        self.status_code = status_code
        self.retorno_servico = retorno_servico
        mensagem = retorno_servico
        super().__init__(self.status_code, mensagem)
