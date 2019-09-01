#Arthur Stevam
#Sábado, 31 de Agosto de 2019
#Classe Notas

class Nota():

    def __init__(self, args):
        self.nota = args[0]
        if args[1] == False:
            self.peso = False
        else:    
            self.peso = args[1]/100

    def __str__(self):
        return self.nota

    def getNota(self):
        if self.peso != False:
            peso_nota = self.nota * self.peso        
            return peso_nota
        else:
            return self.nota
