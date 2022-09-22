import Usuario.findUsuario as buscarUsuarios
from bson.objectid import ObjectId

def cancelarCompra(mydb):
    compra_collection = mydb.compras
    usuario_collection = mydb.usuarios
    compra,usuario = buscarUsuarios.findCompraById(mydb)
    print(compra)
    usuario_collection.update_one({"_id":ObjectId(usuario["_id"]),"compras._id":ObjectId(compra["_id"])},{ "$set": { "compras.$.status":"cancelado" }}, upsert=True)
    compra_collection.update_one({"_id":ObjectId(compra["_id"])},{ "$set": { "status":"cancelado" }}, upsert=True)
    print(f'\nCompra de id {compra["_id"]} cancelado com sucesso')