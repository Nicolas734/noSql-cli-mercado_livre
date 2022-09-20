import pymongo
import Produto.create as createProduto
import Cases.caseUsuario as caseUsuario


client = pymongo.MongoClient("mongodb+srv://Nicolas:senha@nicolas.yt3g1l9.mongodb.net/?retryWrites=true&w=majority")

mydb = client.mercado_livre

execucao = True

while execucao:

    print('''\nOpções: \n
        [1] Usuario
        [2] Cadastrar Produto
        [0] Sair
        ''')

    opcoes = input(str("Escolha uma das opções:"))

    match opcoes:
        case "1":
            caseUsuario.caseUse(mydb)
        case "2":
            createProduto.insertProduto(mydb)
        case "0":
            execucao = False
            print("\nAté mais \n")
            break;