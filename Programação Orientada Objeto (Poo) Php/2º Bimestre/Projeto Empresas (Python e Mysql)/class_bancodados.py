import mysql.connector

class BancoDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='127.0.0.1', user='root', passwd='0207', database = 'empresa')
        self.cursor = self.conexao.cursor()

        #cria a tabela 'produto' se não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS empresa (
                id_empresa INTEGER PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(50) NOT NULL,
                endereco VARCHAR(50) NOT NULL,
                contato VARCHAR(50) NOT NULL,
                ramo_atividade VARCHAR(50) NOT NULL,
                telefone VARCHAR(50) NOT NULL               
            )                            
        """)
    def inserir_empresa(self, empresa):
        self.cursor.execute("""
            INSERT INTO empresa (nome, endereco, contato, ramo_atividade, telefone)
            VALUES (%s, %s, %s, %s, %s)                          
        """, (empresa.nome, empresa.endereco, empresa.contato, empresa.ramo_atividade, empresa.telefone)) #Substitiu pelos %s
        self.conexao.commit() #salva no bd

    def listar_empresas(self):
        self.cursor.execute("""
            SELECT id_empresa, nome, endereco, contato, ramo_atividade, telefone FROM empresa
        """)
        return self.cursor.fetchall()  #buscatodos
    
    def atualizar_empresa(self, empresa, empresa_id):
        self.cursor.execute("""
            UPDATE empresa SET
                nome = %s,
                endereco = %s,
                contato = %s,
                ramo_atividade = %s,
                telefone = %s
            WHERE id_empresa = %s
        """, (empresa.nome, empresa.endereco, empresa.contato, empresa.ramo_atividade, empresa.telefone, empresa_id))
        self.conexao.commit()
    
    def deletar_empresa(self, empresa_id):
        self.cursor.execute("""
            DELETE FROM empresa WHERE id_empresa = %s
    """, (empresa_id,))
        self.conexao.commit()
