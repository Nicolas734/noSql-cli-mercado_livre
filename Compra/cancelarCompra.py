import Usuario.findUsuario as buscarUsuarios
from bson.objectid import ObjectId

def cancelarCompra(mydb):
    compra_collection = mydb.compras
    usuario_collection = mydb.usuarios
    compra = buscarUsuarios.findCompraById(mydb)
    usuario_collection.update_one({"_id":ObjectId(compra["_id"])},{ "$set": { "status":"cancelada" }})
    compra_collection.delete_one({"_id":ObjectId(compra["_id"])})
    
    print(f'\nCompra de id {compra["_id"]} cancelado com sucesso')