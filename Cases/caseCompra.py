import Compra.realizar_pedido as realizar
import Compra.findCompra as buscar
import Compra.cancelarCompra as cancelar

def caseCompra(mydb):
    
    executando = True
    while executando:
        print('''Opções:
        [1] Realizar compra
        [2] Listar todas as compras
        [3] Listar compra por id
        [4] Cancelar compra
        [0] Voltar
            ''')
        
        opcao = input(str("Escolha uma das opções: "))
        
        match opcao:
            case "1":
                realizar.realizar_compra(mydb)
            case "2":
                buscar.findAll(mydb)
            case "3":
                buscar.findById(mydb)
            case "4":
                cancelar.cancelarCompra(mydb)
            case "0":
                return