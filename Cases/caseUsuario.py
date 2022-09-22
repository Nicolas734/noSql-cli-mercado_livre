import Usuario.createUsuario as createUsuario
import Usuario.findUsuario as buscar
import Usuario.updateUsuario as updateUsuario
import Usuario.deleteUsuario as deleteUsuario
from bson.objectid import ObjectId

def caseUse(mydb):
    
    execucao = True
    while execucao:
        print('''Opções: \n
        [1] Cadastrar Usuario
        [2] Buscar todos os usuarios
        [3] Buscar todos os usuarios em ordem alfabética
        [4] Buscar usuario por id
        [5] Listar todas as compras de um usuario
        [6] Listar por id a compra de um usuario
        [7] Atualizar usuario
        [8] Excluir usuario
        [0] Voltar ao Menu
        ''')
        
        opcoes = input(str("Escolha uma das opções: "))
        
        match opcoes:
            case "1":
                createUsuario.cadastrarUsuario(mydb)
            case "2":
                buscar.findAll(mydb)
            case "3":
                buscar.findSort(mydb)
            case "4":
                buscar.findById(mydb)
            case "5":
                buscar.findCompra(mydb)
            case "6":
                buscar.findCompraById(mydb)
            case "7":
                updateUsuario.update(mydb)
            case "8":
                deleteUsuario.deletar(mydb)
            case "0":
                return