from bson.objectid import ObjectId
import Compra.findCompra as buscarCompras

def findAll(mydb):
    mycol = mydb.usuarios
    mydoc = mycol.find()
    print('\n')
    print('--  Lista de usuarios  --\n')
    for x in mydoc:
        print(f'id: {x["_id"]}')
        print(f'Nome: {x["nome"]}')
        print(f'Email: {x["email"]}')
        print(f'Telefone: {x["telefone"]}')
        print(f'CPF: {x["cpf"]}')
        print(f'RG: {x["rg"]}')
        print(f'Data de nascimento: {x["data_nascimento"]}')
        print("\n----------------------------------------\n")


def findById(mydb):
    findAll(mydb)
    userId = input(str("\nDigite o id do usuario desejado: "))
    mycol = mydb.usuarios
    myquery = {"_id":ObjectId(userId)}
    usuario = mycol.find_one(myquery)
    print(f'\n--  Usuario de id {userId}  --\n')
    print(f'Nome: {usuario["nome"]}')
    print(f'Email: {usuario["email"]}')
    print(f'Telefone: {usuario["telefone"]}')
    print(f'CPF: {usuario["cpf"]}')
    print(f'RG: {usuario["rg"]}')
    print(f'Data de nascimento: {usuario["data_nascimento"]}\n')
    return usuario


def findSort(mydb):
    mycol = mydb.usuarios
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(f'id: {x["_id"]}')
        print(f'Nome: {x["nome"]}')
        print(f'Email: {x["email"]}')
        print(f'Telefone: {x["telefone"]}')
        print(f'CPF: {x["cpf"]}')
        print(f'RG: {x["rg"]}')
        print(f'Data de nascimento: {x["data_nascimento"]}')
        print("\n----------------------------------------\n")


def findCompra(mydb):
    usuario = findById(mydb)
    for compra in usuario["compras"]:
        print("\n----------------------------------------\n")
        print(f'--  Compra de id {compra["_id"]}  --\n')
        print("- Produtos da compra\n")
        for produto in compra["produtos"]:
            print(f'Id do produto: {produto["_id"]}')
            print(f'Nome: {produto["nome"]}')
            print(f'Preço: {produto["preco"]}')
        print("\n- Dados da compra\n")
        print(f'Data da compra: {compra["data_compra"]}')
        print(f'Formato do pagamento: {compra["formato_pagamento"]}')
        print(f'Total da compra: {compra["total"]}')
        print("\n----------------------------------------\n")


def findCompraById(mydb):
        compra_collection = mydb.compras
        usuario = findById(mydb)
        for compra in usuario["compras"]:
            print(f'Id: {compra["_id"]}  --\n')
            print(f'Data da compra: {compra["data_compra"]}')
            print(f'Formato do pagamento: {compra["formato_pagamento"]}')
            print(f'Total da compra: {compra["total"]}')
        compra_id = input(str("Digite o id da compra desejada: "))
        compra = compra_collection.find_one({"_id":ObjectId(compra_id)})
        return compra