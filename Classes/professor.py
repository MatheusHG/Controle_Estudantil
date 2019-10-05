#Matheus Henrique
#05/10/19

class Professor():
    __matricula = ""
    __senha = ""
    __turma = []

    def __init__(self, senha, matricula):
        self.__matricula = matricula 
        self.__senha = senha
