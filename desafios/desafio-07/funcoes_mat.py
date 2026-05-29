# Desafio 07 — Bio-Calculadora
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (28/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────


import math

def area_circulo(raio):
    """Calcula a área de um círculo usando o raio informado."""
    return math.pi * raio ** 2

def volume_esfera(raio):
    """Calcula o volume de uma esfera usando o raio informado."""
    return (4 / 3) * math.pi * raio ** 3

def hipotenusa(cateto_a, cateto_b):
    """Calcula a hipotenusa usando os dois catetos."""
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)