from datetime import date

def insertProduto(mydb):
    mycol = mydb.produtos

    print('Cadastro de Produto\n')
    nome = input(str("Digite o nome do produto: "))
    descricao = input(str("Digite a descrição do produto: "))
    preco = input(str("Digite o preço do produto: "))
    qtd = input(str("Digite a quantidade do produto em estoque: "))
    dataAtual = date.today()
    dataFormatada = dataAtual.strftime('%d/%m/%Y')

    mydict = {
        "nome":nome,
        "data_postagem":dataFormatada,
        "descricao":descricao,
        "preco":preco,
        "quantidade":qtd,
        "vendedor":{}
    }

    x = mycol.insert_one(mydict)
    print("\nProduto cadastrado com sucesso\n")
    print(f'Id do produto cadastrado {x.inserted_id}\n')