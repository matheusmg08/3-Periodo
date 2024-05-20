import mysql.connector

class BancoDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='127.0.0.1', user='root', passwd='0207', database = 'poo')
        self.cursor = self.conexao.cursor()

        #cria a tabela 'clientes' se não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL UNIQUE,
                telefone VARCHAR(50) NOT NULL               
            )                            
        """)
    def inserir_cliente(self, cliente):
        self.cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (%s, %s, %s)                          
        """, (cliente.nome, cliente.email, cliente.telefone)) #Substitiu pelos ???
        self.conexao.commit() #salva no bd

    def listar_clientes(self):
        self.cursor.execute("""
            SELECT id, nome, email, telefone FROM clientes
        """)
        return self.cursor.fetchall()  #buscatodos
    
    def atualizar_cliente(self, cliente, cliente_id):
        self.cursor.execute("""
            UPDATE clientes SET
                nome = %s,
                email = %s,
                telefone = %s
            WHERE id = %s
        """, (cliente.nome, cliente.email, cliente.telefone, cliente_id))
        self.conexao.commit()
    
    def deletar_cliente(self, cliente_id):
        self.cursor.execute("""
            DELETE FROM clientes WHERE id = %s
    """, (cliente_id,))
        self.conexao.commit()
