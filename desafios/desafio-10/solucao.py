# Desafio 10 — Projeto Final — Urna Eletrônica
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (28/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
class Candidato:
    def __init__(self, numero, nome, cargo):
        self.numero = numero
        self.nome = nome
        self.cargo = cargo
        self.votos = 0

    def receber_voto(self):
        self.votos += 1

    def exibir_dados(self):
        print(f"{self.numero} - {self.nome} - {self.cargo} - Votos: {self.votos}")


class UrnaEletronica:
    def __init__(self):
        self.candidatos = {}
        self.votos_brancos = 0
        self.votos_nulos = 0

    def cadastrar_candidato(self, candidato):
        self.candidatos[candidato.numero] = candidato

    def votar(self, numero):
        if numero == "branco":
            self.votos_brancos += 1
            print("Voto em branco confirmado.")
        elif numero in self.candidatos:
            self.candidatos[numero].receber_voto()
            print("Voto confirmado.")
        else:
            self.votos_nulos += 1
            print("Voto nulo.")

    def exibir_resultado(self):
        print("Resultado da votação")

        for candidato in self.candidatos.values():
            candidato.exibir_dados()

        print(f"Votos brancos: {self.votos_brancos}")
        print(f"Votos nulos: {self.votos_nulos}")


urna = UrnaEletronica()

urna.cadastrar_candidato(Candidato("10", "Ana Silva", "Presidente"))
urna.cadastrar_candidato(Candidato("20", "Carlos Souza", "Presidente"))
urna.cadastrar_candidato(Candidato("30", "Maria Lima", "Presidente"))

while True:
    print()
    print("Urna Eletrônica")
    print("Digite o número do candidato")
    print("Digite branco para votar em branco")
    print("Digite fim para encerrar")

    voto = input("Seu voto: ").lower()

    if voto == "fim":
        break

    urna.votar(voto)

print()
urna.exibir_resultado()