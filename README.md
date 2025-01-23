# Playlist Python
Este script foi desenvolvido como um exercício prático para explorar os conceitos fundamentais da Programação Orientada a Objetos (POO) em Python. O objetivo é simular uma aplicação que gerencia filmes e séries, organizando-os em uma playlist e permitindo interações como incrementos de likes.

## Conceitos de POO Aplicados

#### Classes e Objetos:
Foram criadas classes como Programa, Filme e Serie para representar entidades do mundo real.
Os objetos instanciados dessas classes (ex.: vingadores, atlanta) são exemplos concretos dessas entidades, cada um com seus próprios atributos e comportamentos.

#### Herança:
A classe Filme e a classe Serie herdam da classe base Programa, aproveitando atributos e métodos genéricos e adicionando características exclusivas, como duracao (em Filme) e temporadas (em Serie).

#### Encapsulamento:
Atributos como _nome e _likes foram definidos como privados (com _ no início) para controlar o acesso direto a eles.
Métodos getter e setter foram criados para acessar e modificar os atributos de forma controlada, garantindo boas práticas e segurança.

#### Polimorfismo:
O método __str__ foi sobrescrito em Filme e Serie, alterando a forma como os objetos dessas classes são representados em texto. Apesar de herdarem o método da classe mãe, cada classe filha tem uma implementação própria.

#### Métodos e Propriedades:
Foram utilizados métodos personalizados, como dar_like, para encapsular a lógica de incrementar likes.
O uso do decorador @property permite acessar atributos como nome e likes diretamente, sem chamar explicitamente métodos, proporcionando uma interface mais limpa.

#### Composição:
A classe Playlist é um exemplo de composição, onde uma playlist é composta por uma lista de objetos Programa (ou suas subclasses). Essa abordagem reutiliza funcionalidades de listas, tornando o código mais eficiente e legível.

## Funcionalidades do Script
- Criação de Filmes e Séries: Cada objeto possui informações como nome, ano de lançamento, duração (para filmes) ou número de temporadas (para séries).
- Sistema de Likes: Permite dar likes a filmes e séries, contabilizando a popularidade de cada um.
- Playlist Personalizável: Organize filmes e séries em uma playlist e navegue pelos itens com facilidade.
- Representação Personalizada: As informações de cada programa são exibidas de maneira clara e legível graças ao polimorfismo.

## Funcionalidades

- Gerenciar filmes e séries.
- Criar playlists com objetos de classes personalizadas.
- Incrementar likes para filmes e séries.

