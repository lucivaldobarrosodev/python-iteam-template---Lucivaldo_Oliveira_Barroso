# Desafio 01 — Seu Primeiro Script
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (19/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
titulo = ("Seja Bem Vindo ao cadatro online")
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nacimento: "))
hobbies = input("Quais seus Hobbies: ")

idade = 2026 - ano_nascimento

print(titulo)
print(f"Olá {nome}, seja bem vindo. sua idade é {idade} anos, e seus principais hobbies são: {hobbies}.")
