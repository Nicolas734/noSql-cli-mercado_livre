def deletar(mydb, ObjectId):
    mycol = mydb.usuarios
    myquery = { "_id": ObjectId("632764bd1d5fcdb328241abe")}
    mycol.delete_one(myquery)