# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: Lucivaldo Oliveira Barroso
# Data: 24/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
try:
    nome = input("Digite seu nome completo: ")
    cpf = input("Digite seu CPF: ")
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    altura = float(input("Digite sua altura: "))

    idade = 2026 - ano_nascimento

    print()
    print("Ficha de cadastro")
    print(f"Nome completo: {nome}")
    print(f"CPF: {cpf}")
    print(f"Ano de nascimento: {ano_nascimento}")
    print(f"Idade em 2026: {idade} anos")
    print(f"Altura: {altura} metros")

except ValueError:
    print("Erro: o ano de nascimento deve ser um número inteiro e a altura deve ser um número.")
# Explicação: A altura é representada como um número decimal (por exemplo, 1.75 metros), o que requer o uso de float para permitir casas decimais. O int não seria adequado, pois não poderia representar alturas com precisão.