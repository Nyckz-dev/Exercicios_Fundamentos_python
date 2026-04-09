from Aluno import aluno
from Calculation import calculation
import NotaInvalidaError

class Program:
    def ler_notas(self, msg):
        while True:
            try:
                nota = float(input(msg))
                if nota < 0 or nota > 10:
                    raise NotaInvalidaError(nota)
                return nota
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except NotaInvalidaError as e:
                print(e)

    def main(self):
        nome = input(f"Digite o nome do aluno: ")
        note1 = self.ler_notas("Digite a primeira nota: ")
        note2 = self.ler_notas("Digite a segunda nota: ")
        note3 = self.ler_notas("Digite a terceira nota: ")

        p = aluno(nome, note1, note2, note3)
        calc = calculation(p)

        print("Aluno: ", p.nome)
        print(f"Média total: {calc.average():.2f}")
        print("Status: ", calc.status())

if __name__ == "__main__":
            Program().main()