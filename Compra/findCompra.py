from bson.objectid import ObjectId

def findAll(mydb):
    compra_collection = mydb.compras
    for compra in compra_collection.find():
        print(compra)