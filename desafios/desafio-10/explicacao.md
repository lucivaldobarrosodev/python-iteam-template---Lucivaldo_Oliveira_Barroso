# Explicação — Desafio 10 — Projeto Final — Urna Eletrônica

**Aluno:** _(Lucivaldo Oliveira Barroso)_  
**Data:** _(28/05/2026)_
---

---

## O que meu programa faz

_(Simula uma urna eletrônica simples. Ele cadastra alguns candidatos, recebe o voto pelo número digitado e soma os votos de cada um.

Também permite votar em branco e considera nulo quando o número não existe. No final, mostra o resultado com os votos dos candidatos, votos brancos e votos nulos.)_

---

## Resposta à Pergunta Obrigatória

> Responda às três perguntas abaixo (cada uma em um parágrafo):
1. Como a herança ou dicionários facilitaram o cadastro de candidatos na sua solução?
2. Como você garantiu que o voto permanecesse anônimo e seguro?
3. Qual foi o maior obstáculo técnico que você superou e como resolveu?

_(
    1. Dicionários facilitam o cadastro dos candidatos, porque cada candidato fica associado ao seu número. Assim, quando o eleitor digita um número, o programa consegue procurar rapidamente se aquele candidato existe. Também usei classes para organizar melhor as informações e os comportamentos da urna e dos candidatos.

    2. O voto permanece anônimo porque o programa não guarda o nome ou qualquer dado do eleitor. Ele registra apenas a quantidade de votos de cada candidato, além dos votos brancos e nulos. Dessa forma, não existe ligação entre uma pessoa e o voto escolhido.

    3. O maior obstáculo técnico foi organizar a votação sem misturar todas as informações em variáveis soltas. Resolvi isso criando uma classe para o candidato e outra para a urna. Assim, cada parte do sistema ficou com uma responsabilidade: o candidato guarda seus dados e votos, e a urna controla o cadastro, a votação e o resultado.)_

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
