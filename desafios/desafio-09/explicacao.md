# Explicação — Desafio 09 — Sistema de Frota

**Aluno:** _(Lucivaldo Oliveira Barroso)_  
**Data:** _(28/05/2026)_
---

---

## O que meu programa faz

_(Meu programa cria uma classe pai chamada `Veiculo`, que guarda informações comuns como marca, ano e quilometragem.

Depois, criei duas classes filhas: `Caminhao` e `Moto`. Elas herdam os dados principais de `Veiculo`, mas também possuem informações próprias. O caminhão tem capacidade de carga e a moto tem cilindradas.

O método `rodar(km)` altera a quilometragem de forma controlada, sem permitir acesso direto ao atributo `__quilometragem`.
)_

---

## Resposta à Pergunta Obrigatória

> Por que `Caminhao` e `Moto` 'herdam de' `Veiculo` e não simplesmente repetem os atributos? O que você ganha e o que arrisca ao usar herança?

_(`Caminhao` e `Moto` herdam de `Veiculo` pois possuem informações em comum. Com herança, evitamos repetir o mesmo código em várias classes.

Deixamos o código mais organizado, reaproveitável e fácil de manter. Se uma regra comum mudar, podemos alterar na classe pai. O risco é usar herança em situações erradas, deixando o código dependente demais da classe pai ou criando uma estrutura mais complicada do que o necessário.
)_

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
