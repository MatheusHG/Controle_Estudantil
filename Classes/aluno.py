#Arthur Stevam 
#Sexta - Feira, 30 de Agosto de 2019
#Classe Aluno

from nota import Nota

class Aluno():

    def __init__(self, nome, data_nascimento,
                numero_cpf, numero_rg):
        self.nome = nome
        self.data_nascimento = str(data_nascimento)
        self.numero_cpf = numero_cpf
        self.numero_rg = numero_rg
        self.matricula = f"20191{self.numero_cpf:.03s}"
        self.estado_do_aluno = True
        self.aprovado = None
        self.notas = []
        self.faltas = 0
        self.qtd_notas = 0

    def __str__(self): 
        s = ('Aluno: {}\n'.format(self.nome) 
             + 'Data de Nascimento: {}\n'.format(self.data_nascimento)
             + 'Matrícula: {}'.format(self.matricula))
        return s
   
    def adicionarNota(self, n, peso):
        nota = Nota([n, peso])
        self.notas.append(nota)
        self.qtd_notas += 1

    ## Tipo media == 1 quando calculo com peso e 0 quando não.
    def getMedia(self, quantidade_notas, tipo_media):
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
        return l

    def adicionarFalta(self):
        self.faltas += 1

    def abonarFalta(self):
        self.faltas -= 1

    def getFaltas(self):
        return self.faltas
