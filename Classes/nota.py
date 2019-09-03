#Arthur Stevam
#Sábado, 31 de Agosto de 2019
#Classe Notas

class Nota():

    def __init__(self, nota, peso):
        self.nota = nota
        self.peso = peso

    def __str__(self):
        return self.nota

    def recebeidentidade(self, n):
        self.nota = n[3]
        self.peso = n[4]
