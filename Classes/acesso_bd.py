import sqlite3

class banco_de_dados():
    
    def __init__(self):
        # conectar ao bd
        conn = sqlite3.connect('sistema_alunos.db')
        #definindo um cursor
        cursor = conn.cursor()

        #criando tabela alunos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                matricula VARCHAR(8) NOT NULL PRIMARY KEY UNIQUE,
                nome TEXT NOT NULL,
                rg VARCHAR(15) NOT NULL UNIQUE,
                cpf VARCHAR(14) NOT NULL UNIQUE,
                estado INTEGER NOT NULL,
                aprovado INTEGER NOT NULL,
                faltas INTEGER NOT NULL
            );""")

        #criando tabela turma
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS turma (
                codigo VARCHAR(9) NOT NULL UNIQUE PRIMARY KEY,
                estado INTEGER NOT NULL,
                faltas INTEGER 
            );""")

        #criando tabela relação turma/aluno
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS matricula (
                matricula_aluno VARCHAR(8) NOT NULL UNIQUE,
                codigo_turma VARCHAR(9) NOT NULL UNIQUE,
                quantidade_notas INTEGER NOT NULL,
                FOREIGN KEY (matricula_aluno) REFERENCES aluno(matricula),
                FOREIGN KEY (codigo_turma) REFERENCES turma(codigo)
            );""")

        #criando tabela de alunos na final
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS finalista (
                matricula_aluno VARCHAR(8) NOT NULL UNIQUE,
                codigo_turma VARCHAR(9) NOT NULL UNIQUE,
                FOREIGN KEY (matricula_aluno) REFERENCES aluno(matricula),
                FOREIGN KEY (codigo_turma) REFERENCES turma(codigo)
            );""")

        #criando tabela de relação aluno/nota
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nota (
                matricula_aluno VARCHAR(8) NOT NULL UNIQUE,
                nota REAL NOT NULL,
                peso INTEGER NOT NULL,
                FOREIGN KEY (matricula_aluno) REFERENCES aluno(matricula)
            );""")

    
    def desconecta(self):
        conn.close()
