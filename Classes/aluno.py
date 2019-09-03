#Arthur Stevam 
#Sexta - Feira, 30 de Agosto de 2019
#Classe Aluno

from Classes.nota import Nota

class Aluno():

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.matricula = f"20191{self.cpf:.03s}"
        self.aprovado = False
        #self.qtd_notas = 0

    ## Tipo media == 1 quando calculo com peso e 0 quando não.
    '''def getMedia(self, quantidade_notas, tipo_media):
        if quantidade_notas != self.qtd_notas:
            return False
        soma_das_notas = 0
        soma_pesos = 0
        quantidade_sem_peso = 0 
        for n in self.notas:
            if (n.peso != False):
                soma_pesos += n.peso
            else:
                quantidade_sem_peso += 1
        if (tipo_media == 1):
            if quantidade_sem_peso != 0:
                peso_restou = (1.0 - soma_pesos) / quantidade_sem_peso
            for n in self.notas:
                if(n.peso == False):
                    n.peso = peso_restou
                soma_das_notas += n.getNota()
            self.media = soma_das_notas
        else:
            for n in self.notas:
                soma_das_notas += n.getNota()
            self.media = soma_das_notas/len(self.notas)
        return self.media

    def getNotas(self):
        l = []
        for n in self.notas:
            l.append(n.getNota())
        return l '''

    def recebeentidade(self, a):
        self.matricula = a[0]
        self.nome = a[1]
        self.cpf = a[2]
        self.aprovado = a[3]

    def notafinal(self, n):
        self.final = n
