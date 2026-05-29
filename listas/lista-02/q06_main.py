# Lista 02 — Questão 06: Módulo de Estatísticas (programa principal)
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
import q06_estatisticas as estatisticas

notas = []

for contador in range(1, 11):
    while True:
        try:
            nota = float(input(f"Digite a {contador}ª nota: "))

            if nota >= 0 and nota <= 10:
                notas.append(nota)
                break
            else:
                print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite um número válido.")

print()
print(f"Média: {estatisticas.media(notas)}")
print(f"Mediana: {estatisticas.mediana(notas)}")
print(f"Moda: {estatisticas.moda(notas)}")
print(f"Desvio padrão: {estatisticas.desvio_padrao(notas)}")