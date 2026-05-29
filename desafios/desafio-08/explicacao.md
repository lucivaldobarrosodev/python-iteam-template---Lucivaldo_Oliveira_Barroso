# Explicação — Desafio 08 — Banco Digital

**Aluno:** _(Lucivaldo Oliveira Barroso)_  
**Data:** _(28/05/2026)_
---

---

## O que meu programa faz

_(Meu programa cria uma classe chamada `ContaBancaria`. Ela recebe o nome do titular e o saldo inicial.

A classe possui um método para depositar dinheiro, outro para sacar e outro para exibir o extrato. O saque só acontece se houver saldo suficiente na conta.
)_

---

## Resposta à Pergunta Obrigatória

> Por que `saldo` deve ser um **atributo da instância** (`self.saldo`) e não uma variável comum dentro do método? O que mudaria no comportamento do programa?

_(O saldo deve ser um atributo da instância, usando `self.saldo`, porque ele precisa continuar existindo dentro do objeto mesmo depois que um método termina.

Se o saldo fosse apenas uma variável comum dentro de um método, ele existiria somente naquele momento e seria perdido depois. Com `self.saldo`, cada conta guarda seu próprio saldo e os métodos conseguem consultar e alterar esse valor corretamente.
)_

---

## Dificuldades encontradas

_(Minha maior atenção foi entender que `self.saldo` pertence ao objeto, enquanto uma variável comum pertence apenas ao método onde foi criada.)_
