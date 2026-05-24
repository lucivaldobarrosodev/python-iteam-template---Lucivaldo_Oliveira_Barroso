# Desafio 06 — Bio-Cadastro
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (24/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
equipe = []

while True:
    nome = input("Digite o nome do colaborador ou 'sair' para encerrar: ")

    if nome.lower() == "sair":
        break

    cargo = input("Digite o cargo do colaborador: ")

    funcionario = {
        "nome": nome,
        "cargo": cargo
    }

    equipe.append(funcionario)

print()
print("Lista de funcionários:")

for funcionario in equipe:
    print(f"Funcionário: {funcionario['nome']} | Cargo: {funcionario['cargo']}")