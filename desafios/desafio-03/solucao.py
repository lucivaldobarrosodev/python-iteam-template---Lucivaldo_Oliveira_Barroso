# Desafio 03 — Sistema de Multas
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (19/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
velocidade = float(input("Digite a velocidade atual do seu veiculo: "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7

    print("Você foi multado por exceder o limite da via, que é de 80 km/h")
    \n
    print(f"Valor da multa é de: {multa: .2f}")

else:
    print("Boa Viagem! Dirija com segurança.")    