#Arthur Stevam 
#Sexta - Feira, 30 de Agosto de 2019
#Classe Aluno

from Classes.nota import Nota
from bd.acesso_bd import banco_de_dados

class Aluno():
    __nome = ""
    __cpf = ""
    __matricula = ""
    __media = 0
    __notas = []

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__matricula = f"20191{self.__cpf:.03s}"
        self.__notas = []
        self.__media = 0

    def recebeentidade(self, a):
        self.__matricula = a[0]
        self.__nome = a[1]
        self.__cpf = a[2]
        self.__media = a[3]

    def salvar(self):
        bd = banco_de_dados()
        try:
            bd.insertaluno(self.__matricula, self.__nome, self.__cpf, self.__media)
            print('Aluno matriculado com sucesso!')
        except:
            print('Não foi possível salvar o aluno. Tente novamente mais tarde!')

    def getmedia(self):
        soma = 0
        tipo = 0
        quantidade = 0
        self.__getnotas()
        for nota in self.__notas:
            if nota.get_peso() == 0 or tipo == 1:
                quantidade += 1
                soma += nota.get_nota()
                tipo = 1
            else:
                soma += (nota.get_nota() * nota.get_peso())/100
        if tipo == 1:
            self.__media = soma/quantidade
        else:
            self.__media = soma
        return self.__media

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def __getnotas(self):
        self.__notas.clear()
        bd = banco_de_dados()
        result = bd.getnotasaluno(self.__matricula)
        nota = Nota(0, 0, 0)
        try:
            for n in result:
                nota.recebeentidade(n)
                self.__notas.append(nota)
        except:
            print('Erro ao tentar recuperar notas!')

    def get_matricula(self):
        return self.__matricula


