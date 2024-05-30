from class_bancodados import BancoDados
from class_empresa import Empresa
def cadastrar_empresa():
    nome = input("Digite o nome da empresa: ")
    endereco = input("Digite o endereço da empresa: ")
    contato = input("Digite o contato da empresa: ")
    ramo_atividade = input("Digite o ramo de atividade da empresa: ")
    telefone = int(input("Digite o telefone da empresa: "))

    nova_empresa = Empresa(nome, endereco, contato, ramo_atividade, telefone)
    Banco_Dados.inserir_empresa(nova_empresa)
    print("Empresa cadastrada com sucesso!")

def listar_empresas():
    empresas = Banco_Dados.listar_empresas()
    for empresa in empresas:
        print (f"ID: {empresa[0]} | Nome: {empresa[1]} | Endereço: {empresa[2]} | Contato: {empresa[3]} | Ramo de atividade: {empresa[4]} | Telefone: {empresa[5]}")

def atualizar_empresa():
    id_empresa = int(input("Digite o ID da empresa a ser atualizada: "))
    novo_nome = input("Digite o novo nome da empresa: ")
    novo_endereco = input("Digite o novo endereço da empresa: ")
    novo_contato = input("Digite o novo contato da empresa: ")
    novo_ramo_atividade = input("Digite o novo ramo de atividade da empresa: ")
    novo_telefone = input("Digite o novo telefone da empresa: ")
    empresa_atualizada = Empresa(novo_nome, novo_endereco, novo_contato, novo_ramo_atividade, novo_telefone)
    Banco_Dados.atualizar_empresa(empresa_atualizada, id_empresa)
    print ("Empresa atualizada com sucesso!")

def deletar_empresa():
    id_empresa = int(input("Digite o ID da empresa a ser deletada: "))
    Banco_Dados.deletar_empresa(id_empresa)
    print ("Empresa deletada com sucesso !")

Banco_Dados = BancoDados()

while True:
    print ("\nMenu Principal: ")
    print ("1. Cadastrar Empresas")
    print ("2. Listar Empresas")
    print ("3. Atualizar Empresas")
    print ("4. Deletar Empresas")
    print ("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        cadastrar_empresa()
    elif opcao == '2':
        listar_empresas()
    elif opcao == '3':
        atualizar_empresa()
    elif opcao == '4':
        deletar_empresa()
    elif opcao == '0':
        print ('Saindo ...')
        break
    else:
        print ("Opção inválida !")

Banco_Dados.conexao.close()