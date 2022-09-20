import Produto.findProduto as findProduto
from bson.objectid import ObjectId

def deleteProduto(mydb):
    mycol = mydb.produtos
    findProduto.findAll(mydb)
    id = input(str("Por favor digite o Id do produto que deseja excluir: "))
    mycol.delete_one({"_id": ObjectId(id)})
    print(f'\nProduto de id {id} excluido com sucesso\n')