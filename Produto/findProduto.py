from bson.objectid import ObjectId

def findAll(mydb):
    mycol = mydb.produtos
    print('\n')
    print('---  Lista de produtos  ---\n')
    for x in mycol.find():
        print(f'id: {x["_id"]}')
        print(f'Nome: {x["nome"]}')
        print(f'Descrição: {x["descricao"]}')
        print(f'Preço: {x["preco"]}')
        print(f'Quantidade em estoque: {x["quantidade"]}')
        print(f'Data de Postagem: {x["data_postagem"]}')
        print("\n----------------------------------------\n")


def findById(mydb):
    mycol = mydb.produtos
    findAll(mydb)
    id = input(str("\nEscolha o id de um produto: "))
    produto = mycol.find_one({"_id":ObjectId(id)})
    print(f'\n--  Produto de id {id}  --\n')
    print(f'Nome: {produto["nome"]}')
    print(f'Descrição: {produto["descricao"]}')
    print(f'Preço: {produto["preco"]}')
    print(f'Quantidade em estoque: {produto["quantidade"]}')
    print(f'Data de Postagem: {produto["data_postagem"]}')
    print("\n----------------------------------------\n")
    return produto

def findSort(mydb):
    mycol = mydb.produtos
    print('\n')
    print('---  Lista de produtos  ---\n')
    for x in mycol.find().sort("nome"):
        print(f'id: {x["_id"]}')
        print(f'Nome: {x["nome"]}')
        print(f'Descrição: {x["descricao"]}')
        print(f'Preço: {x["preco"]}')
        print(f'Quantidade em estoque: {x["quantidade"]}')
        print(f'Data de Postagem: {x["data_postagem"]}')
        print("\n----------------------------------------\n")