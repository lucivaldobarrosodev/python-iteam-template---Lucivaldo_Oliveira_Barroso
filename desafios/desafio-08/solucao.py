# Desafio 08 — Banco Digital
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (28/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso.")

    def exibir_extrato(self):
        print("Extrato da conta")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


conta = ContaBancaria("Lucivaldo Oliveira Barroso", 500)

conta.exibir_extrato()
conta.depositar(200)
conta.sacar(100)
conta.sacar(1000)
conta.exibir_extrato()