# Desafio 07 — Bio-Calculadora
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (28/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
from funcoes_mat import area_circulo, volume_esfera, hipotenusa

print("Bio-Calculadora")
print("1 - Área do círculo")
print("2 - Volume da esfera")
print("3 - Hipotenusa")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    raio = float(input("Digite o raio: "))
    resultado = area_circulo(raio)
    print(f"Área do círculo: {resultado:.2f}")

elif opcao == "2":
    raio = float(input("Digite o raio: "))
    resultado = volume_esfera(raio)
    print(f"Volume da esfera: {resultado:.2f}")

elif opcao == "3":
    cateto_a = float(input("Digite o primeiro cateto: "))
    cateto_b = float(input("Digite o segundo cateto: "))
    resultado = hipotenusa(cateto_a, cateto_b)
    print(f"Hipotenusa: {resultado:.2f}")

else:
    print("Opção inválida.")