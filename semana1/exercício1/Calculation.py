from Aluno import aluno
class calculation:

    def __init__(self, p):
        self.p = p

    def sum(self):
        return self.p.note1 + self.p.note2 + self.p.note3

    def average(self):
        return self.sum() / 3
    
    def status(self):
        if self.average() >= 7:
            return "Aprovado"
        elif self.average() >= 5:
            return "Recuperação"
        else:
            return "Reprovado"