import NotaInvalidaError
class aluno:
    
    def __init__(self, nome, note1, note2, note3):
        for nota in [note1, note2, note3]:
            if nota < 0 or nota > 10:
                raise NotaInvalidaError(nota)
            
        self.nome = nome
        self.note1 = note1
        self.note2 = note2
        self.note3 = note3

    