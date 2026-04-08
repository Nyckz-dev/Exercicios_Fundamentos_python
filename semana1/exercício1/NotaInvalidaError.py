class NotaInvalidaError(Exception):
    def __init__(self, valor):
        super().__init__(f"Nota inválida: {valor}. A nota deve estar entre 0 e 10.")