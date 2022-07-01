from classe_fabricante import *
from classe_produto import *

class Estoque:
    def __init__(self):
        self.listaCadastro = []
        self.listaFabri = [] 


    def salvar_produtos(self):
        entrada = input('Digite o código do fabricante:')
        for i in range(len(self.listaFabri)):
            if entrada == self.listaFabri[i].codi:
                entrada_cod = input('código do produto: ')
                entrada_descricao = input('descrição do produto: ')
                entrada_fabri = print()
                entrada_quant = int(input('quantidade: '))
                self.listaCadastro.append(Produto(entrada_cod, entrada_descricao, entrada_fabri, entrada_quant))
                print('Cadastro realizado!')


    def listar_todos_produtos(self):
        entrada = input('código do produto:')
        for i in range(len(self.listaCadastro)):
            if entrada == self.listaCadastro[i].cod:
                print('--- Cod:',self.listaCadastro[i].cod,
                      '- Descrição:',self.listaCadastro[i].descricao,
                      '- Fabricante:',self.listaFabri[i].nome,
                      '- Quantidade:',self.listaCadastro[i].quant)
                
        if entrada == '':
            for i in range(len(self.listaCadastro)):
                print('--- Cod:',self.listaCadastro[i].cod,
                          '- Descrição:',self.listaCadastro[i].descricao,
                          '- Fabricante:',self.listaFabri[i].nome,
                          '- Quantidade:',self.listaCadastro[i].quant)
                
        else:
            print('Fim da listagem')
        
    def alterar_produto(self):
        entrada = input('código do produto: ')
        for i in range(len(self.listaCadastro)):
            if entrada == self.listaCadastro[i].cod:
                self.listaCadastro[i].descricao = input('descrição do produto: ')
                print('Alteração realizada!')


    def cadastrar_fabri(self):
        entrada_codi = input('código do fabricante: ')
        entrada_nome = input('nome do fabricante: ')
        self.listaFabri.append(Fabricante(entrada_codi,entrada_nome))
        print('Cadastro realizado!')
