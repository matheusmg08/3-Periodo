from class_bancodados import BancoDados
from class_produto import Produto
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))
    quantidade = int(input("Digite a quantidade do produto: "))
    novo_produto = Produto(nome, preco, quantidade)
    Banco_Dados.inserir_produto(novo_produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    produtos = Banco_Dados.listar_produtos()
    for produto in produtos:
        print (f"ID: {produto[0]} | Nome: {produto[1]} | Preço: {produto[2]} | Quantidade: {produto[3]}")

def atualizar_produto():
    produto_id = int(input("Digite o ID do produto a ser atualizado: "))
    novo_nome = input("Digite o novo nome do produto: ")
    novo_preco = input("Digite o novo preço do produto: ")
    novo_quantidade = input("Digite a nova quantidade do produto: ")
    produto_atualizado = Produto(novo_nome, novo_preco, novo_quantidade)
    Banco_Dados.atualizar_produto(produto_atualizado, produto_id)
    print ("Produto atualizado com sucesso!")

def deletar_produto():
    produto_id = int(input("Digite o ID do produto a ser deletado: "))
    Banco_Dados.deletar_produto(produto_id)
    print ("Produto deletado com sucesso !")

Banco_Dados = BancoDados()

while True:
    print ("\nMenu Principal: ")
    print ("1. Cadastrar Produtos")
    print ("2. Listar Produtos")
    print ("3. Atualizar Produtos")
    print ("4. Deletar Produtos")
    print ("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        atualizar_produto()
    elif opcao == '4':
        deletar_produto()
    elif opcao == '0':
        print ('Saindo ...')
        break
    else:
        print ("Opção inválida !")

Banco_Dados.conexao.close()