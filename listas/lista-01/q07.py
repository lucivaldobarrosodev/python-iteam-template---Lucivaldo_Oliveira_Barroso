# Lista 01 — Questão 07: Progressão e Análise
# Aluno: Lucivaldo Oliveira Barroso
# Data: 24/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
notas = []

# Usei for porque a quantidade de notas é conhecida: são 10 notas.
for contador in range(1, 11):
    while True:
        try:
            nota = float(input(f"Digite a {contador}ª nota: "))

            if nota >= 0 and nota <= 10:
                notas.append(nota)
                break
            else:
                print("A nota deve estar entre 0.0 e 10.0.")

        except ValueError:
            print("Digite um valor numérico válido.")

maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)
acima_da_media = 0

# Usei for aqui porque preciso percorrer todas as notas da lista.
for nota in notas:
    if nota > media:
        acima_da_media += 1

print()
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Média: {media:.2f}")
print(f"Quantidade acima da média: {acima_da_media}")

if media >= 7.0:
    print("Classificação: Aprovado")
elif media >= 5.0:
    print("Classificação: Recuperação")
else:
    print("Classificação: Reprovado")

# Usei while na validação porque não sei quantas tentativas o usuário vai precisar
# até digitar uma nota válida.