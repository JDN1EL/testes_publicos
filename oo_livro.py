class Livro:
    def __init__(self,nome, qtd_paginas, autor, preco):
        self.nome = nome.title()
        self.qtd_paginas = qtd_paginas
        self.autor = autor.title()
        self.preco = preco

    @property
    def titulo(self):
        return print(f'Nome: {self.nome}')

    @property
    def pag(self):
        return print(f'Paginas: {self.qtd_paginas}')

    @property 
    def eu_lirico(self):
        return print(f'Autor: {self.autor}')

    @property
    def valor(self):
        return print(f'Valor: R${self.preco}')
#MÉTODOS¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
    @property
    def getpreco(self):
        return self.preco

    @getpreco.setter
    def set_preco(self,novo_valor):
        self.preco = novo_valor
        print(f'\nNovo valor adicionado de: R${novo_valor}\n')
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
banca = Livro('sherlock Holmes: O Cão dos Beskwiles',200,'Sur Arthur',77)
banca.titulo
banca.pag
banca.eu_lirico
banca.valor

banca.set_preco = 90
