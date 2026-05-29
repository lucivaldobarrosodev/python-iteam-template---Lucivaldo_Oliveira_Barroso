# Lista 02 — Questão 05: Funções de Alta Ordem
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q05.py: escreva aplicar(lista, funcao) que retorna uma nova lista com a
# função aplicada a cada elemento. Demonstre com:
#   (a) função que eleva ao quadrado
#   (b) função que retorna True se o número for par
# 
# Em q05_resposta.txt: explique o que significa dizer que funções são
# 'cidadãs de primeira classe' em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
def aplicar(lista, funcao):
    nova_lista = []

    for item in lista:
        nova_lista.append(funcao(item))

    return nova_lista

def ao_quadrado(numero):
    return numero ** 2

def eh_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5]

print(aplicar(numeros, ao_quadrado))
print(aplicar(numeros, eh_par))