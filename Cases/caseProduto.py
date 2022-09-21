import Produto.createProduto as createProduto
import Produto.findProduto as findProduto
import Produto.deleteProduto as deleteProduto
import Produto.updateProduto as atualizar_produto

def caseProd(mydb):
    
    execucao = True
    while execucao:
        print('''Opções: \n
        [1] Cadastrar Produto
        [2] Buscar todos os produtos
        [3] Buscar todos os produtos em ordem alfabética
        [4] Buscar produto por id
        [5] Atualizar produto
        [6] Excluir produto
        [0] Voltar
        ''')

        opcoes = input (str("Escolha uma das opções: "))
        
        match opcoes:
            case "1":
                createProduto.insertProduto(mydb)
            case "2":
                findProduto.findAll(mydb)
            case "3":
                findProduto.findSort(mydb)
            case "4":
                findProduto.findById(mydb)
            case "5":
                atualizar_produto.atualizarProduto(mydb)
            case "6":
                deleteProduto.deleteProduto(mydb)
            case "0":
                return