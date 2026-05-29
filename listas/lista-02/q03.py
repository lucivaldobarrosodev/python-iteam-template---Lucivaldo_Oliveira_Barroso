# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: (Lucivaldo Oliveira Barroso)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    produto = {
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade,
        "preco": preco
    }
    inventario.append(produto)

def buscar_por_codigo(inventario, codigo):
    for produto in inventario:
        if produto["codigo"] == codigo:
            return produto
    return None

def listar_abaixo_do_minimo(inventario, minimo):
    produtos_baixos = []
    for produto in inventario:
        if produto["quantidade"] < minimo:
            produtos_baixos.append(produto)
    return produtos_baixos

def valor_total(inventario):
    total = 0
    for produto in inventario:
        total += produto["quantidade"] * produto["preco"]
    return total

inventario = []

adicionar_produto(inventario, "Arroz", "001", 10, 25.50)
adicionar_produto(inventario, "Feijão", "002", 4, 8.90)
adicionar_produto(inventario, "Macarrão", "003", 2, 5.75)

print("Inventário:")
print(inventario)

print("Buscar produto:")
print(buscar_por_codigo(inventario, "002"))

print("Produtos abaixo do mínimo:")
print(listar_abaixo_do_minimo(inventario, 5))

print(f"Valor total: R$ {valor_total(inventario):.2f}")