# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (28/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
def mostrar_candidatos(candidatos):
    print("Candidatos cadastrados:")

    for candidato in candidatos.values():
        print(f"{candidato.numero} - {candidato.nome} - {candidato.cargo}")


def mostrar_resultado(candidatos, votos_brancos, votos_nulos):
    print("Resultado da votação")
    print()

    for candidato in candidatos.values():
        print(candidato.exibir_dados())

    print(f"Votos brancos: {votos_brancos}")
    print(f"Votos nulos: {votos_nulos}")