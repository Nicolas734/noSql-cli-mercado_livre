import Compra.realizar_pedido as realizar
import Compra.findCompra as buscar

def caseCompra(mydb):
    
    executando = True
    while executando:
        print('''Opções:
        [1] Realizar compra
        [2] Listar compras de um cliente
        [3] Listar todas as compras
        [4] Cancelar compra
        [0] Voltar
            ''')
        
        opcao = input(str("Escolha uma das opções: "))
        
        match opcao:
            case "1":
                realizar.realizar_compra(mydb)
            case "2":
                print('')
            case "3":
                buscar.findAll(mydb)
            case "4":
                print("")
            case "0":
                return