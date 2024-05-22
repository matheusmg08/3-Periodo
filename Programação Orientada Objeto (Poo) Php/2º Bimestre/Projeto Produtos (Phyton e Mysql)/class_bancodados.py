import mysql.connector

class BancoDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='127.0.0.1', user='root', passwd='0207', database = 'produto')
        self.cursor = self.conexao.cursor()

        #cria a tabela 'produto' se não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id_produto INTEGER PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(50) NOT NULL,
                preco FLOAT NOT NULL,
                quantidade INT NOT NULL               
            )                            
        """)
    def inserir_produto(self, produto):
        self.cursor.execute("""
            INSERT INTO produto (nome, preco, quantidade)
            VALUES (%s, %s, %s)                          
        """, (produto.nome, produto.preco, produto.quantidade)) #Substitiu pelos %s
        self.conexao.commit() #salva no bd

    def listar_produtos(self):
        self.cursor.execute("""
            SELECT id_produto, nome, preco, quantidade FROM produto
        """)
        return self.cursor.fetchall()  #buscatodos
    
    def atualizar_produto(self, produto, produto_id):
        self.cursor.execute("""
            UPDATE produto SET
                nome = %s,
                preco = %s,
                quantidade = %s
            WHERE id_produto = %s
        """, (produto.nome, produto.preco, produto.quantidade, produto_id))
        self.conexao.commit()
    
    def deletar_produto(self, produto_id):
        self.cursor.execute("""
            DELETE FROM produto WHERE id_produto = %s
    """, (produto_id,))
        self.conexao.commit()
