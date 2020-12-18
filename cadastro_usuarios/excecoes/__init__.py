class CadastroUsuarioException(Exception):
    def __init__(self, status_code: int, mensagem: str):
        self.status_code = status_code
        self.mensagem = mensagem


class CamposObrigatoriosException(CadastroUsuarioException):
    def __init__(self, classe: str, campo: str, status_code: int = 416):
        self.status_code = status_code
        mensagem = f"{classe}: {campo} não informado"
        super().__init__(self.status_code, mensagem)
