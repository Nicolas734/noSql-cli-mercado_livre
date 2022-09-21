import Vendedor.findVendedor as buscarVendedor
from bson.objectid import ObjectId

def atualizarVendedor(mydb):
    vend_collection  = mydb.vendedores
    vendedor_id = buscarVendedor.findById(mydb)
    
    execucao = True
    while execucao:
        
        print('''--- Opções de atualização ---
        [1] Nome
        [2] Email
        [3] Telefone
        [0] Finalizar
        ''')
        
        opcao = input("\nEscolha o que deseja atualizar: ")
        
        match opcao:
            case "1":
                nome = input(str("Digite o novo nome do vendedor: "))
                vend_collection.update_one({"_id":ObjectId(vendedor_id["_id"])},{ "$set": { "nome":nome }})
            case "2":
                email = input(str("Digite o novo email do vendedor: "))
                vend_collection.update_one({"_id":ObjectId(vendedor_id["_id"])},{ "$set": { "email":email }})
            case "3":
                telefone = input(str("Digite o novo telefone do vendedor: "))
                vend_collection.update_one({"_id":ObjectId(vendedor_id["_id"])},{ "$set": { "telefone":telefone }})
            case "0":
                execucao = False
                vendedor = vend_collection.find_one({"_id":ObjectId(vendedor_id["_id"])})
                print(f'\n--  Vendedor de id {vendedor_id["_id"]}  --\n')
                print(f'Nome: {vendedor["nome"]}')
                print(f'CNPJ: {vendedor["cnpj"]}')
                print(f'Email: {vendedor["email"]}')
                print(f'Telefone: {vendedor["telefone"]}')