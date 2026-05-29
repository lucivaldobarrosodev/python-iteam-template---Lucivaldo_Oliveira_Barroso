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
        return f"{self.numero} - {self.nome} - {self.cargo} - Votos: {self.votos}"