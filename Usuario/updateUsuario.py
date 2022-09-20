import Usuario.findUsuario as findUsuario

def update(mydb, ObjectId):
    mycol = mydb.usuarios
    execucao = True
    findUsuario.findAll(mydb)
    id = input(str("Por favor digite o Id do usuario que deseja atualizar: "))
    myquery = {"_id":ObjectId(id)}
    
    while execucao:
        print('''--- Opções de atualização ---
            [1] Nome
            [2] Email
            [3] Telefone
            [4] Data de nascimento
            [0] Finalizar
            ''')
        
        opcao = input("\nEscolha o que deseja atualizar: ")
        
        match opcao:
            case "1":
                nome = input(str("Digite seu novo nome: "))
                mycol.update_one(myquery,{ "$set": { "nome":nome }})
                print("\nNome atualizado com sucesso.")
            case "2":
                email = input(str("Digite seu novo email: "))
                mycol.update_one(myquery,{ "$set": { "email":email }})
                print("\nEmail atualizado com sucesso.")
            case "3":
                telefone = input(str("Digite seu novo telefone: "))
                mycol.update_one(myquery,{ "$set": { "telefone":telefone }})
                print("\nTelefone atualizado com sucesso.")
            case "4":
                data_nascimento = input(str("Digite a data de nascimento: "))
                mycol.update_one(myquery,{ "$set": { "data_nascimento":data_nascimento }})
                print("\nData de nascimento atualizada com sucesso.")
            case "0":
                execucao = False
                print('\nDados atualizados com sucesso\n')
                print(f'Novos dados do usuario {id}\n')
                mycol.find(myquery)
                for x in mycol.find(myquery):

                    print(f'Nome: {x["nome"]}')
                    print(f'Email: {x["email"]}')
                    print(f'Telefone: {x["telefone"]}')
                    print(f'CPF: {x["cpf"]}')
                    print(f'RG: {x["rg"]}')
                    print(f'Data de nascimento: {x["data_nascimento"]}\n')
                return