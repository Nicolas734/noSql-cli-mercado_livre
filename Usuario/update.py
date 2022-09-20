def update(mydb, ObjectId):
    mycol = mydb.usuarios
    myquery = {"_id":ObjectId("632764bd1d5fcdb328241abe")}
    newValues = { "$set": { "nome":"pinguinha" }}
    mydoc = mycol.update_one(myquery,newValues)
    for x in mycol.find():
        print(x)