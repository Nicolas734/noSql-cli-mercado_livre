import Vendedor.findVendedor as buscar
from bson.objectid import ObjectId

def deleteVendedor(mydb):
    buscar.findAll(mydb)
    id = input(str("Por favor digite o Id do vendedor que deseja excluir: "))
    mycol = mydb.vendedores
    mycol.delete_one({"_id": ObjectId(id)})
    print(f'\nVendedor de id {id} excluido com sucesso\n')