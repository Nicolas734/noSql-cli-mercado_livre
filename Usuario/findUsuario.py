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

def findById(mydb,ObjectId):
    findAll(mydb)
    userId = input(str("\nEscolha o id de um usuario: "))
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