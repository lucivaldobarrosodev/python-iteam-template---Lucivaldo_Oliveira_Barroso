# Projeto Integrador — Urna Eletrônica
# Aluno: (LUCIVALDO OLIVEIRA BARROSO)
# Data:  (28/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────

from candidatos import Candidato
from relatorio import mostrar_candidatos, mostrar_resultado


class UrnaEletronica:
    def __init__(self):
        self.candidatos = {}
        self.votos_brancos = 0
        self.votos_nulos = 0

    def cadastrar_candidato(self, candidato):
        self.candidatos[candidato.numero] = candidato

    def votar(self, voto):
        if voto == "branco":
            self.votos_brancos += 1
            print("Voto em branco confirmado.")
        elif voto in self.candidatos:
            self.candidatos[voto].receber_voto()
            print("Voto confirmado.")
        else:
            self.votos_nulos += 1
            print("Voto nulo.")

    def exibir_candidatos(self):
        mostrar_candidatos(self.candidatos)

    def exibir_resultado(self):
        mostrar_resultado(self.candidatos, self.votos_brancos, self.votos_nulos)


urna = UrnaEletronica()

urna.cadastrar_candidato(Candidato("10", "Ana Silva", "Presidente"))
urna.cadastrar_candidato(Candidato("20", "Carlos Souza", "Presidente"))
urna.cadastrar_candidato(Candidato("30", "Maria Lima", "Presidente"))

while True:
    print()
    print("Urna Eletrônica")
    print("1 - Ver candidatos")
    print("2 - Votar")
    print("3 - Encerrar votação")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        urna.exibir_candidatos()

    elif opcao == "2":
        print()
        urna.exibir_candidatos()
        print("Digite branco para votar em branco.")
        voto = input("Digite seu voto: ").lower()
        urna.votar(voto)

    elif opcao == "3":
        break

    else:
        print("Opção inválida.")

print()
urna.exibir_resultado()