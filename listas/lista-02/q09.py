# Lista 02 — Questão 09: Encapsulamento e Propriedades
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q09.py — classe Produto com:
#   1. __preco via @property com validação (preço > 0)
#   2. __estoque com getter, repor(qtd) e vender(qtd) — ValueError se sem estoque
#   3. __str__ informativo e __repr__ para debug
# Demonstre: criação, vendas, reposição e tentativa de venda além do estoque.
# 
# Em q09_resposta.txt: explique a diferença entre _atributo e __atributo em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = valor

    @property
    def estoque(self):
        return self.__estoque

    def repor(self, qtd):
        if qtd <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self.__estoque += qtd

    def vender(self, qtd):
        if qtd <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if qtd > self.__estoque:
            raise ValueError("Estoque insuficiente.")
        self.__estoque -= qtd

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} - Estoque: {self.estoque}"

    def __repr__(self):
        return f"Produto(nome={self.nome}, preco={self.preco}, estoque={self.estoque})"

produto = Produto("Teclado", 120.00, 10)

print(produto)
produto.vender(3)
print(produto)

produto.repor(5)
print(produto)

try:
    produto.vender(20)
except ValueError as erro:
    print(erro)

print(repr(produto))