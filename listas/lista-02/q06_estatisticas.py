# Lista 02 — Questão 06: Módulo de Estatísticas (módulo estatísticas)
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# q06_estatisticas.py: crie o módulo com as funções:
#   media(dados), mediana(dados), moda(dados), desvio_padrao(dados)
# Todas devem: receber lista de floats, validar que não está vazia
# (lançar ValueError se estiver), retornar resultado arredondado (2 casas).
# Use apenas stdlib (math permitido, não use statistics).
# 
# q06_main.py: importe o módulo e aplique as 4 funções sobre 10 notas
# digitadas pelo usuário.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
import math

def validar(dados):
    if len(dados) == 0:
        raise ValueError("A lista não pode estar vazia.")

def media(dados):
    validar(dados)
    return round(sum(dados) / len(dados), 2)

def mediana(dados):
    validar(dados)
    ordenados = sorted(dados)
    tamanho = len(ordenados)
    meio = tamanho // 2

    if tamanho % 2 == 1:
        return round(ordenados[meio], 2)

    return round((ordenados[meio - 1] + ordenados[meio]) / 2, 2)

def moda(dados):
    validar(dados)
    mais_repetido = dados[0]
    maior_quantidade = 0

    for valor in dados:
        quantidade = dados.count(valor)
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            mais_repetido = valor

    return round(mais_repetido, 2)

def desvio_padrao(dados):
    validar(dados)
    m = media(dados)
    soma = 0

    for valor in dados:
        soma += (valor - m) ** 2

    variancia = soma / len(dados)
    return round(math.sqrt(variancia), 2)