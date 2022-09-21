import Usuario.findUsuario as buscarUsuarios
import Produto.findProduto as buscarProdutos
from bson.objectid import ObjectId

def adicionar_favoritos(mydb):
    user_collection = mydb.usuarios
    
    usuario = buscarUsuarios.findById(mydb)
    execucao = True
    
    while execucao:
        
        opcao = input(str("Deseja adicionar um produto aos favoritos ? "))
        
        if opcao.lower() == 'sim':
            produto = buscarProdutos.findById(mydb)
            user_collection.update_one({"_id":ObjectId(usuario["_id"])},{ "$push":{ "lista_favoritos":produto } })
        else:
            execucao = False
    
    print("\nProduto adicionado aos favoritos.\n")