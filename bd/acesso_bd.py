import sqlite3

class banco_de_dados():

    def __init__(self):
        # conectar ao bd
        self.conn = sqlite3.connect('sistema_alunos.db')
        #definindo um cursor
        self.cursor = self.conn.cursor()

        #criando tabela alunos
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                matricula VARCHAR(8) NOT NULL PRIMARY KEY UNIQUE,
                nome VARCHAR NOT NULL,
                cpf VARCHAR(14) NOT NULL UNIQUE,
                media REAL 
            );""")

        #criando tabela turma
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS turma (
                codigo VARCHAR(9) NOT NULL UNIQUE PRIMARY KEY,
                faltas INTEGER, 
                quantidade_notas INTEGER
            );""")

        #criando tabela relação turma/aluno
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS matriculado (
                matricula_aluno VARCHAR(8) NOT NULL UNIQUE,
                codigo_turma VARCHAR(9) NOT NULL,
                FOREIGN KEY (matricula_aluno) REFERENCES aluno(matricula),
                FOREIGN KEY (codigo_turma) REFERENCES turma(codigo)
                PRIMARY KEY (matricula_aluno, codigo_turma)
            );""")

        #criando tabela de relação aluno/nota
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS nota (
                id INTEGER NOT NULL,
                matricula_aluno VARCHAR(8) NOT NULL,
                codigo_turma VARCHAR(9) NOT NULL,
                nota REAL NOT NULL,
                peso INTEGER NOT NULL,
                FOREIGN KEY (matricula_aluno) REFERENCES aluno(matricula),
                FOREIGN KEY (codigo_turma) REFERENCES turma(codigo),
                PRIMARY KEY (id, matricula_aluno)
            );""")

    def insertnota(self, id, matricula_aluno, codigo_turma, nota, peso):
        self.cursor.execute("""
            INSERT INTO nota (id, matricula_aluno, codigo_turma, nota, peso)
            VALUES (?, ?, ?, ?, ?)
        """, (id, matricula_aluno, codigo_turma, nota, peso))
        self.conn.commit()

    def insertaluno(self, matricula, nome, cpf, media):
        self.cursor.execute("""
            INSERT INTO alunos (matricula, nome, cpf, media)
            VALUES (?, ?, ?, ?)
        """, (matricula, nome, cpf, media))
        self.conn.commit()

    def getaluno(self, matricula):
        result =self.cursor.execute("""
            SELECT * FROM alunos WHERE matricula = ?
        """, (matricula,))
        return result.fetchone()

    def getalunos(self, codigo):
        result =self.cursor.execute("""
            SELECT * FROM matriculado WHERE codigo_turma = ?
        """, (codigo,))
        return result.fetchall()

    def gettodosalunos(self):
        result =self.cursor.execute("""
            SELECT * FROM alunos
        """)
        return result.fetchall()

    def getturmas(self):
        result = self.cursor.execute("""
            SELECT * FROM turma
        """)
        return result.fetchall()

    def getturma(self, codigo):
        result = self.cursor.execute("""
            SELECT * FROM turma WHERE codigo = ?
        """, (codigo,))
        return result.fetchone()

    def getnotasaluno(self, matricula_aluno):
        result = self.cursor.execute("""
            SELECT * FROM nota WHERE matricula_aluno = ?
        """, (matricula_aluno,))
        return result.fetchall()

    def insertturma(self, codigo, faltas,  notas):
        self.cursor.execute("""
            INSERT INTO turma (codigo, faltas, quantidade_notas)
            VALUES (?, ?, ?)
        """, (codigo, faltas, notas))
        self.conn.commit()

    def insertmatricula(self, matricula_aluno, codigo_turma):
        self.cursor.execute("""
            INSERT INTO matriculado (matricula_aluno, codigo_turma)
            VALUES (?, ?)
        """, (matricula_aluno, codigo_turma))
        self.conn.commit()

    def updatequantidadenotas(self, codigo, quantidade):
        self.cursor.execute("""
                UPDATE turma
                SET quantidade_notas = ?
                WHERE codigo = ? 
        """, (quantidade, codigo))
        self.conn.commit()

    def deleteturma(self, codigo):
        self.cursor.execute("""
            DELETE FROM turma WHERE codigo = ?
        """, (codigo, ))
        self.conn.commit()

    def deletealuno(self, matricula):
        self.cursor.execute("""
            DELETE FROM alunos WHERE matricula = ?
        """, (matricula,))
        self.conn.commit()

    def desconecta(self):
        self.conn.close()
