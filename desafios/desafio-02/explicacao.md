# Explicação — Desafio 02 — Calculadora de IMC

**Aluno:** _(Lucivaldo Oliveira Barroso)_  
**Data:** _(19/05/2026)_
---

## O que meu programa faz

_
- Var nome recebe a string do imput.
- var peso e altura devem ter a o float por se tratarem de numeros que podem receber casas decimais.
- Na var IMC temos o calculo de peso dividico por altura ao quadrado representado pelos dois (*)
- Na frase de resultado com o f-string para poder ter as variaveis na frase temos o {imc:.2f} que mostar o resultado com duas casas decimais_

---

## Resposta à Pergunta Obrigatória

> Por que é necessário usar `float()` ao capturar peso e altura com `input()`? O que aconteceria se usássemos `int()` para a altura `1.75`?

_ Pois se usassemos o int ele não iria dar erro pois ele não consegue receber os numeros com casa decimais, por isso devemos colocar o float, para que possamos fazer essa captura com casas decimais_

---

## Dificuldades encontradas

_Procurei na internet com apoio da IA sobre as duas casas decimais no final {imc:.2f}_
