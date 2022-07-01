from classe_estoque import *
from classe_controle import *
from classe_saida import *


class Menu:
    def __init__(self):
        estoque = Estoque()
        compra = Compra()
        saida = Saida()
        compra.entrada = estoque
        saida.entrada2 = estoque

        while True:
            entrada_fab = input('[1] - Cadastrar Fabricante\n[2] - Fabricante já existente\n')
            if entrada_fab == '1':
                estoque.cadastrar_fabri()
            elif entrada_fab == '2':
                entrada2 = input('[1] - Cadastrar Produto\n[2] - Listar todos\n[3] - Alterar Produto\n[4] - Comprar do estoque\n[5] - Saida do produto\n[6] - Sair\n')
                if entrada2 == '1':
                    estoque.salvar_produtos()
                elif entrada2 == '2':
                    estoque.listar_todos_produtos()
                elif entrada2 == '3':
                    estoque.alterar_produto()
                elif entrada2 == '4':
                    compra.comprar_produtos()
                elif entrada2 == '5':
                    saida.sair_produtos()
                elif entrada2 == '6':
                    print('Operação Finalizada')
                    break
                else:
                    print('Invalido!')
            else:
                    print('invalido!')
