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


def findById(mydb,ObjectId):
    mycol = mydb.vendedores
    findAll(mydb)
    id = input(str("\nEscolha o id do vendedor: "))
    for x in mycol.find({"_id":ObjectId(id)}):
        print(f'\n--  Vendedor de id {id}  --\n')
        print(f'Nome: {x["nome"]}')
        print(f'CNPJ: {x["cnpj"]}')
        print(f'Email: {x["email"]}')
        print(f'Telefone: {x["telefone"]}')
        print("\n----------------------------------------\n")

def findSort(mydb):
    mycol = mydb.vendedores
    print('\n')
    print('---  Lista de vendedores  ---\n')
    for x in mycol.find().sort():
        print(f'id: {x["_id"]}')
        print(f'Nome: {x["nome"]}')
        print(f'CNPJ: {x["cnpj"]}')
        print(f'Email: {x["email"]}')
        print(f'Telefone: {x["telefone"]}')
        print("\n----------------------------------------\n")