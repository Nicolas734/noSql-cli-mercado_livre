import Produto.findProduto as buscarProdutos
import Vendedor.findVendedor as buscarVendedores
from bson.objectid import ObjectId

def designar(mydb):
    prod_collection = mydb.produtos
    vend_collection = mydb.vendedores
    
    vendedor = buscarVendedores.findById(mydb)
    executando = True
    
    while executando:
        
        selecionar_produto = input(str(f'deseja cadastrar um produto ao vendedor ? '))
        
        if selecionar_produto.lower() == "sim":
            buscarProdutos.findAll(mydb)
            produto_id = input(str("Digite o id do produto que deseja cadastrar: "))
            produto = prod_collection.find_one({"_id":ObjectId(produto_id)})
            prod_collection.update_one({"_id":ObjectId(produto_id)},{ "$set": { "vendedor":vendedor }})
            vend_collection.update_one({"_id":ObjectId(vendedor["_id"])},{ "$push": { "produtos":produto }})
        else:
            executando = False
    
    for x in prod_collection.find():
        print(x)