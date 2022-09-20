def cadastrarUsuario(mydb):

    print("Cadastro do Usuario \n")
    nome = input(str("Digite seu nome: "))
    email = input(str("Digite seu email: "))
    telefone = input(str("Digite seu telefone: "))
    cpf = input(str("Digite seu CPF: "))
    rg = input(str("Digite seu RG: "))
    nascimento = input(str("Digite sua Data de Nascimento: "))
    print('\n')

    enderecos = cadastrarEndereco()

    mycol = mydb.usuarios
    mydict = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "cpf": cpf,
        "rg": rg,
        "data_nascimento": nascimento,
        "enderecos":enderecos,
        "lista_favoritos":[],
        "compras":[]
    }
    x = mycol.insert_one(mydict)
    print("\nUsuario cadastrado com sucesso")
    print(f'Id do usuario cadastrado {x.inserted_id}')


def cadastrarEndereco():
    execucao = True
    enderecos = []
    print("Cadastro de endereço\n")

    while execucao:
        
        opcao = input(str("Deseja cadastrar um endereco ? "))
        if opcao.lower() == 'sim':
            estado = input(str("Digite o estado: "))
            cep = input(str("Digite o CEP: "))
            cidade = input(str("Digite a cidade: "))
            bairro = input(str("Digite o bairro: "))
            rua = input(str("Digite a rua: "))
            numero  = input(str("Digite o numero: "))
            complemento = input(str("Digite o complemento: "))
            print('\n')
            enderecos.append({"estado":estado,"cep":cep,"cidade":cidade,"bairro":bairro,"rua":rua,"numero":numero,"complemento":complemento})
        
        else:
            execucao = False

    return enderecos