from classe_estoque import *


class Compra:
    def __init__(self):
        self.entrada = Estoque()


    def comprar_produtos(self):
        controle = int(input('código do produto:'))
        for i in range(len(self.entrada.listaCadastro)):
            if controle == self.entrada.listaCadastro[i].cod:
                self.entrada.listaCadastro[i].quant += int((input('quantidade comprada:')))
                print('Quantidade alterada!')


            else:
                pass
        