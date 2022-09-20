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
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(f'\n--  Usuario de id {userId}  --\n')
        print(f'Nome: {x["nome"]}')
        print(f'Email: {x["email"]}')
        print(f'Telefone: {x["telefone"]}')
        print(f'CPF: {x["cpf"]}')
        print(f'RG: {x["rg"]}')
        print(f'Data de nascimento: {x["data_nascimento"]}\n')

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