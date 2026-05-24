# Desafio 05 — Gerenciador de Compras
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (24/05/2026)
# ── Escreva sua solução abaixo ──────────────────────────────────────────────
compras = []

while True:
    produto = input("Digite o nome de um produto ou 'fim' para encerrar: ")

    if produto.lower() == "fim":
        break

    compras.append(produto)

print()
print("Lista de compras:")

for item in compras:
    print(f"- {item}")

print()
print(f"Total de itens: {len(compras)}")