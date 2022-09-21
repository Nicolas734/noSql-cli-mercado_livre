import Produto.findProduto as buscarProduto
from bson.objectid import ObjectId

def atualizarProduto(mydb):
    prod_collection  = mydb.produtos
    produto_id = buscarProduto.findById(mydb)
    
    execucao = True
    while execucao:
        
        print('''--- Opções de atualização ---
        [1] Nome
        [2] Descriçao
        [3] Preço
        [4] Quantidade
        [0] Finalizar
        ''')
        
        opcao = input("\nEscolha o que deseja atualizar: ")
        
        match opcao:
            case "1":
                nome = input(str("Digite o novo nome do produto: "))
                prod_collection.update_one({"_id":ObjectId(produto_id["_id"])},{ "$set": { "nome":nome }})
            case "2":
                descricao = input(str("Digite a nova descrição do produto: "))
                prod_collection.update_one({"_id":ObjectId(produto_id["_id"])},{ "$set": { "descricao":descricao }})
            case "3":
                preco = input(str("Digite o novo preço do produto: "))
                prod_collection.update_one({"_id":ObjectId(produto_id["_id"])},{ "$set": { "preco":preco }})
            case "4":
                quantidade = input(str("Digite a nova quantidade do produto em estoque: "))
                prod_collection.update_one({"_id":ObjectId(produto_id["_id"])},{ "$set": { "quantidade":quantidade }})
            case "0":
                execucao = False
                print('\nDados atualizados com sucesso\n')
                print(f'Novos dados do usuario {produto_id["_id"]}\n')
                produto = prod_collection.find_one({"_id":ObjectId(produto_id["_id"])})
                print(f'\n--  Produto de id {produto_id["_id"]}  --\n')
                print(f'Nome: {produto["nome"]}')
                print(f'Descrição: {produto["descricao"]}')
                print(f'Preço: {produto["preco"]}')
                print(f'Quantidade em estoque: {produto["quantidade"]}')
                print(f'Data de Postagem: {produto["data_postagem"]}')
                return
            