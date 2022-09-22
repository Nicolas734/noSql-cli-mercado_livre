from bson.objectid import ObjectId

def findAll(mydb):
    compra_collection = mydb.compras
    for compra in compra_collection.find():
        print("--  Lista de compras  --\n")
        print(f'id: {compra["_id"]}')
        print(f'Data da compra: {compra["data_compra"]}')
        print(f'Formato do pagamento: {compra["formato_pagamento"]}')
        print(f'Total da compra: {compra["total"]}')
        print("\n----------------------------------------\n")

def findById(mydb):
    compra_collection = mydb.compras
    findAll(mydb)
    compra_id = input(str("Digite o id da compra que deseja cancelar: "))
    compra = compra_collection.find_one({"_id":ObjectId(compra_id)})
    print(f'\n--  Compra de id {compra["_id"]}  --\n')
    print(f'Data da compra: {compra["data_compra"]}')
    print(f'Formato do pagamento: {compra["formato_pagamento"]}')
    print(f'Total da compra: {compra["total"]}')
    print("\n----------------------------------------\n")
    return compra