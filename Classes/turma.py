#Arthur Stevam
#Sábado, 31 de Agosto de 2019
#Classe Turma

import random
from bd.acesso_bd import banco_de_dados
from Classes.aluno import Aluno

class Turma():
    __limitefaltas = 0
    __codigo_turma = ''
    __quantidade_notas = 0
    __alunos = []

    def __init__(self, faltas):
        __codigo = random.randint(10, 99)
        self.__limitefaltas = faltas
        self.__codigo_turma = f'2019{__codigo}{faltas:02}'
        self.__quantidade_notas = 0

    def get_limitefaltas(self):
        return self.__limitefaltas

    def get_codigo_turma(self):
        return self.__codigo_turma

    def get_quantidade_notas(self):
        return self.__quantidade_notas

    def recebeentidade(self, t):
        self.__codigo_turma = t[0]
        self.__limitefaltas = t[1]
        self.__quantidade_notas = t[2]

    def matricularalunos(self, lista_alunos):
        bd = banco_de_dados()
        try:
            for a in lista_alunos:
                bd.insertmatricula(a.get_matricula(), self.__codigo_turma)
            print(f'{len(lista_alunos)} alunos matriculados.')
        except:
            print('Não foi possível matricular os alunos, tente novamente mais tarde!')

    def infoturma(self):
        self.__setalunos()
        for a in self.__alunos:
            print(a.nome)
        print(f'{len(self.__alunos)} alunos matriculados.')

    def adicionarnotas(self):
        self.__setalunos()
        bd = banco_de_dados()
        try:
            for a in self.__alunos:
                while True:
                    nota = float(input(f'Nota de {a.get_nome()}: '))
                    peso = float(input(f'Peso da nota (0 para média aritmética): '))
                    if 0 <= nota <= 10  and (peso == 0 or 10 <= peso <= 100): break
                bd.insertnota(self.__quantidade_notas, a.get_matricula(), self.__codigo_turma, nota, peso)
                print('-'*50)
            self.__quantidade_notas += 1 
            bd.updatequantidadenotas(self.__codigo_turma, self.__quantidade_notas)
        except:
            print('Erro ao tentar salvar notas. Tente novamente mais tarde!')

    def __setalunos(self):
        self.__alunos.clear()
        bd = banco_de_dados()
        try:
            lista_alunos = bd.getalunos(self.__codigo_turma)
            for a in lista_alunos:
                aluno = Aluno("", "")
                aluno.recebeentidade(bd.getaluno(a[0]))
                self.__alunos.append(aluno)
        except:
            print('Não foi possivel recuperar alunos no momento, tente novamente mais tarde!')

    def encerrarturma(self):
        self.__setalunos()
        bd = banco_de_dados()
        try:
            s = ''
            for a in self.__alunos:
                media = a.getmedia()
                if media >= 7:
                    situacao = 'Aprovado'
                elif media >= 4:
                    situacao = 'Final'
                else:
                    situacao = 'Reprovado'
                s += f'{a.get_nome()} -- Média: {media:.1f} -- {situacao}\n'
            print(s)
            self.__desmatricularalunos()
            bd.deleteturma(self.__codigo_turma)
            save = int(input('Deseja gerar um txt com o relatório final dos alunos? 1-Sim 2-Não'))
            if save == 1:
                name = str(input('Nome do arquivo? '))
                arq = open("{}.txt".format(name), "w", encoding="utf-8")
                arq.write(s)
                arq.close()
        except:
            print('Erro ao tentar encerrar turma. Tente novamente mais tarde!')

    def __desmatricularalunos(self):
        bd = banco_de_dados()
        try:
            for a in self.__alunos:
                bd.deletealuno(a.get_matricula())
        except:
            print('Erro ao desmatricular alunos!')

    def salvar(self):
        bd = banco_de_dados()
        try:
            bd.insertturma(self.__codigo_turma, self.__limitefaltas, self.__quantidade_notas)
            print(f'Turma criada com sucesso!')
        except:
            print('Não foi possível salvar turma. Tente novamente mais tarde!')
