from bson.objectid import ObjectId

def findAll(mydb):
    mycol = mydb.vendedores
    print('\n')
    print('---  Lista de vendedores  ---\n')
    for x in mycol.find():
        print(f'id: {x["_id"]}')
        print(f'Nome: {x["nome"]}')
        print(f'CNPJ: {x["cnpj"]}')
        print(f'Email: {x["email"]}')
        print(f'Telefone: {x["telefone"]}')
        print("\n----------------------------------------\n")


def findById(mydb):
    mycol = mydb.vendedores
    findAll(mydb)
    id = input(str("\nEscolha o id do vendedor: "))
    vendedor = mycol.find_one({"_id":ObjectId(id)})
    print(f'\n--  Vendedor de id {id}  --\n')
    print(f'Nome: {vendedor["nome"]}')
    print(f'CNPJ: {vendedor["cnpj"]}')
    print(f'Email: {vendedor["email"]}')
    print(f'Telefone: {vendedor["telefone"]}')
    print("\n----------------------------------------\n")
    return vendedor

def findSort(mydb):
    mycol = mydb.vendedores
    print('\n')
    print('---  Lista de vendedores  ---\n')
    for x in mycol.find().sort("nome"):
        print(f'id: {x["_id"]}')
        print(f'Nome: {x["nome"]}')
        print(f'CNPJ: {x["cnpj"]}')
        print(f'Email: {x["email"]}')
        print(f'Telefone: {x["telefone"]}')
        print("\n----------------------------------------\n")