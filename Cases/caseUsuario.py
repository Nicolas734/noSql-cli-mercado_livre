import Usuario.create as create
import Usuario.find as find
import Usuario.update as update
import Usuario.delete as delete
from bson.objectid import ObjectId

def caseUse(mydb):
    
    execucao = True
    while execucao:
        print('''Opções: \n
        [1] Cadastrar Usuario
        [2] Buscar todos os usuarios
        [3] Buscar todos os usuarios em ordem alfabética
        [4] Buscar usuario por id
        [5] Atualizar usuario
        [6] Excluir usuario
        [7] Parar Programa
        [0] Voltar ao Menu
        ''')
        
        opcoes = input(str("Escolha uma das opções:"))
        
        match opcoes:
            case "1":
                create.cadastrarUsuario(mydb)
            case "2":
                find.findAll(mydb)
            case "3":
                find.findSort(mydb)
            case "4":
                find.findById(mydb,ObjectId)
            case "5":
                update.update(mydb,ObjectId)
            case "6":
                delete.deletar(mydb,ObjectId)
            case "7":
                print("\nAté mais \n")
                break
            case "0":
                return