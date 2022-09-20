import Produto.findProduto as findProduto

def deleteProduto(mydb,ObjectId):
    mycol = mydb.produtos
    findProduto.findAll(mydb)
    id = input(str("Por favor digite o Id do produto que deseja excluir: "))
    mycol.delete_one({"_id": ObjectId(id)})
    print(f'\nProduto de id {id} excluido com sucesso\n')