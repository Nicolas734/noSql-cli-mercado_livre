def insertProduto(mydb):
    mycol = mydb.produtos
    mydict = {
        "nome":"vaso",
        "data_postagem":"29/07/2022",
        "descricao":"vaso de planta",
        "preco":"32.00",
        "quantidade":"30",''
        "vendedor":{
            "id":"aa23sg24g2fd2hfg13fsad13",
            "nome":"claudio",
            "email":"claudio@gmail.com"
        }
    }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)