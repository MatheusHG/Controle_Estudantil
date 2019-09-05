#Arthur Stevam
#Sábado, 31 de Agosto de 2019
#Classe Notas

from bd.acesso_bd import banco_de_dados

class Nota():
    __nota = 0
    __peso = 0
    __id = 0

    def __init__(self, id, nota, peso):
        self.__id = id
        self.__nota = nota
        self.__peso = peso

    def recebeentidade(self, n):
        self.__id = n[0]
        self.__nota = n[3]
        self.__peso = n[4]

    def get_id(self):
        return self.__id

    def get_peso(self):
        return self.__peso
    
    def get_nota(self):
        return self.__nota

    def salvar(self, codigo_turma, matricula_aluno):
        bd = banco_de_dados()
        try:
            bd.insertnota(self.get_id, matricula_aluno, codigo_turma, self.get_nota, self.get_peso)
        except:
            print('Não foi possível salvar a nota nesse momento. Por favor tente novamente mais tarde!')