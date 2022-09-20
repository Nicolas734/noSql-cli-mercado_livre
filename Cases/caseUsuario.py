import Usuario.createUsuario as createUsuario
import Usuario.findUsuario as findUsuario
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
        [5] Atualizar usuario
        [6] Excluir usuario
        [0] Voltar ao Menu
        ''')
        
        opcoes = input(str("Escolha uma das opções: "))
        
        match opcoes:
            case "1":
                createUsuario.cadastrarUsuario(mydb)
            case "2":
                findUsuario.findAll(mydb)
            case "3":
                findUsuario.findSort(mydb)
            case "4":
                findUsuario.findById(mydb,ObjectId)
            case "5":
                updateUsuario.update(mydb,ObjectId)
            case "6":
                deleteUsuario.deletar(mydb,ObjectId)
            case "0":
                return