import Vendedor.createVendedor as cadastrar
import Vendedor.findVendedor as buscar
from bson.objectid import ObjectId

def caseVendedor(mydb):
    
    execucao = True
    while execucao:
        
        print('''Opções: \n
        [1] Cadastrar vendedor
        [2] Buscar todos os vendedores
        [3] Buscar todos os vendedores em ordem alfabética
        [4] Buscar vendedor por id
        [5] Atualizar vendedor
        [6] Excluir vendedor
        [0] Voltar ao Menu
        ''')
        
        opcoes = input(str("Escolha uma das opções: "))
        
        match opcoes:
            case "1":
                cadastrar.cadastrarVendedor(mydb)
            case "2":
                buscar.findAll(mydb)
            case "3":
                buscar.findSort(mydb)
            case "4":
                buscar.findById(mydb,ObjectId)
            case "5":
                print('futurameete será feito')
            case "6":
                print('futurameete será feito')
            case "0":
                return