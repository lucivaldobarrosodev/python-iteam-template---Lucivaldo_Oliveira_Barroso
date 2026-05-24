# Desafio 04 — Tabuada Personalizada
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (24/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
while True:
    numero = int(input("Digite um número de 1 a 10 para ver a tabuada ou 0 para sair: "))

    if numero == 0:
        print("Programa encerrado.")
        break

    if numero < 1 or numero > 10:
        print("Número inválido. Digite um número entre 1 e 10.")
        continue

    print(f"\nTabuada do {numero}:")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")

    print()