import pymongo
import Cases.caseUsuario as usuario
import Cases.caseProduto as produto
import Cases.caseVendedor as vendedor
import Cases.caseCompra as compra
import Cases.caseFavoritos as favorito
import Designar.designar as designar

client = pymongo.MongoClient("mongodb+srv://Nicolas:senha@nicolas.yt3g1l9.mongodb.net/?retryWrites=true&w=majority")

mydb = client.mercado_livre

execucao = True

while execucao:

    print('''\nOpções: \n
        [1] Usuario
        [2] Produto
        [3] Vendedor
        [4] Designar
        [5] Compra
        [6] Favoritos
        [0] Sair
        ''')

    opcoes = input(str("Escolha uma das opções: "))

    match opcoes:
        case "1":
            usuario.caseUse(mydb)
        case "2":
            produto.caseProd(mydb)
        case "3":
            vendedor.caseVendedor(mydb)
        case "4":
            designar.designar(mydb)
        case "5":
            compra.caseCompra(mydb)
        case "6":
            favorito.case_favoritos(mydb)
        case "0":
            execucao = False
            print("\nAté mais \n")
            break