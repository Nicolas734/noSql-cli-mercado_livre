import Usuario.createUsuario as criarEnderecos

def cadastrarVendedor(mydb):
    mycol = mydb.vendedores
    nome = input(str("Digite seu nome: "))
    cnpj = input(str("Digite o seu cnpj: "))
    email = input(str("Digite seu email: "))
    telefone = input(str("Digite seu telefone: "))
    
    enderecos = criarEnderecos.cadastrarEndereco()
    
    mydict = {
        "nome": nome,
        "cnpj": cnpj,
        "email": email,
        "telefone": telefone,
        "enderecos":enderecos,
        "produtos":[]
    }
    
    x = mycol.insert_one(mydict)
    print("\nVendedor cadastrado com sucesso\n")
    print(f'Id do usuario cadastrado {x.inserted_id}\n')