# Lista 01 — Questão 06: Validador de Senha
# Aluno: Lucivaldo Oliveira Barroso
# Data: 24/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────
tentativas = 0

while True:
    senha = input("Digite uma senha: ")
    tentativas += 1

    tem_tamanho = len(senha) >= 8
    tem_digito = False
    tem_maiuscula = False

    for caractere in senha:
        if caractere.isdigit():
            tem_digito = True
        if caractere.isupper():
            tem_maiuscula = True

    if tem_tamanho and tem_digito and tem_maiuscula:
        print(f"Senha válida após {tentativas} tentativa(s).")
        break

    if not tem_tamanho:
        print("A senha precisa ter no mínimo 8 caracteres.")

    if not tem_digito:
        print("A senha precisa ter pelo menos um dígito.")

    if not tem_maiuscula:
        print("A senha precisa ter pelo menos uma letra maiúscula.")