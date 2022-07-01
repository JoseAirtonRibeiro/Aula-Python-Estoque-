from classe_estoque import *


class Saida:
    def __init__(self):
        self.entrada2 = Estoque()


    def sair_produtos(self):
        controle = int(input('código do produto:'))
        for i in range(len(self.entrada2.listaCadastro)):
            if controle == self.entrada2.listaCadastro[i].cod:
                self.entrada2.listaCadastro[i].quant -= int((input('quantidade comprada:')))
                print('Quantidade alterada!')


            else:
                pass