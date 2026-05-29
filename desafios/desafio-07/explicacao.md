# Explicação — Desafio 07 — Bio-Calculadora

**Aluno:** _(Lucivaldo Oliveira Barroso)_  
**Data:** _(28/05/2026)_
---

## O que meu programa faz

_(Meu programa separa as funções matemáticas em um arquivo chamado `funcoes_mat.py`. Nesse arquivo ficam as funções dos calculos.

No arquivo `solucao.py`, o usuário escolhe qual cálculo deseja fazer. Depois, o programa pede os valores necessários, chama a função correspondente e mostra o resultado formatado.
)_

---

## Resposta à Pergunta Obrigatória

> Por que separar as funções em um arquivo diferente do `solucao.py`? O que muda no projeto quando você tem 50 funções em vez de 3?

_(Separar as funções em outro arquivo deixa o projeto mais organizado. O `solucao.py` fica responsável pela interação com o usuário, enquanto o `funcoes_mat.py` fica responsável pelos cálculos.

Quando o projeto tem apenas 3 funções, ainda é possível deixar tudo no mesmo arquivo. Mas quando temos 50 funções, o código fica grande, confuso e mais difícil de manter. Separando, fica mais fácil encontrar erros, reutilizar funções e organizar melhor o projeto.)_

---

## Dificuldades encontradas

_(Minha maior atenção foi entender como importar as funções de outro arquivo usando `from funcoes_mat import ...`.)_
