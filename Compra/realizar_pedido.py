import Usuario.findUsuario as buscarUsuarios
import Produto.findProduto as buscarProdutos
from bson.objectid import ObjectId
from datetime import date

def realizar_compra(mydb):
    compra_collection = mydb.compras
    user_collection = mydb.usuarios
    
    lista_produtos = []
    usuario = buscarUsuarios.findById(mydb)
    
    data_atual = date.today()
    data_formatada = data_atual.strftime('%d/%m/%Y')
    
    total = 0
    
    execucao = True
    while execucao:
        
        opcao = input(str("Deseja comprar um produto ? "))
        
        if opcao.lower() == "sim":
            produto = buscarProdutos.findById(mydb)
            lista_produtos.append(produto)
            total = total + float(produto["preco"])
        else:
            execucao = False
    
    formato_pagamento = input("digite o formato de pagamento desejado: ")
    
    mydict = {
        "data_compra":data_formatada,
        "formato_pagamento":formato_pagamento,
        "total":total,
        'usuario':usuario,
        "produtos":lista_produtos
    }
    
    compra_id = compra_collection.insert_one(mydict)
    
    compra = compra_collection.find_one({"_id":ObjectId(compra_id.inserted_id)})
    user_collection.update_one({"_id":ObjectId(usuario["_id"])},{ "$push": { "compras":compra }})
    
    print("\nCompra realizada com sucesso")
    print(f'Id da compra {compra_id.inserted_id}')