import Usuario.findUsuario as findUsuario

def deletar(mydb,ObjectId):
    findUsuario.findAll(mydb)
    id = input(str("Por favor digite o Id do usuario que deseja excluir: "))
    mycol = mydb.usuarios
    myquery = {"_id": ObjectId(id)}
    mycol.delete_one(myquery)
    print(f'\nUsuario de id {id} excluido com sucesso\n')