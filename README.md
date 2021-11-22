# Aividade 4 de Prog II

## Sistema Perfumaria ABC

1. Núcleo do código em `main.py`.
2. `funcionalidades.py` possui as funções das funcionalidades requisitadas no trabalho.
3. `funcionarios.py` possui o pedaço de gerencimento do banco de dados referente ao cadastro dos funcionários e `produtos.py` é sobre o gerenciamento do banco de dados dos produtos.
4. `Perfumaria.db` é o banco de dados fornecido pelo professor com a maior parte dos dados já inseridos.

## O que foi pedido pelo professor: 

A Perfumaria ABC solicitou o desenvolvimento de um sistema para poder obter informações referentes aos produtos em estoque. As funcionalidades que devem ser disponibilizadas por este sistema são as seguintes:

a) Listar nome e preço de vendados produtos em ordem alfabética pelo nome.

b) Listar código, nome, saldo em estoque e saldo mínimo de um produto identificado pelo seu código.

c) Listar código, nome, saldo em estoque e saldo mínimo de todos os produtos cujo saldo em estoque esteja menor que o mínimo.

d) Listar código, nome, saldo em estoque e saldo mínimo dos produtos cujo saldo em estoque seja menor que o mínimo, e que tenha preço de venda maior que zero.

e) Listar código, nome, saldo em estoque e saldo mínimo dos produtos com saldo em estoque menor que o mínimo e preço de custo maior que zero.

f) Listar código, nome, saldo em estoque e saldo mínimo dos produtos com saldo em estoque menor que o mínimo e preço de venda maior que zero, em ordem alfabética por nome.

g) Listar código e nome de todos os produtos que estão com preço de venda menor ou igual a zero.

h) Informar quantos produtos estão cadastrados.

i) Informar quantos produtos estão com saldo em estoque zerado.

j) Informar quantos produtos estão com saldo em estoque menor que o mínimo.

k) Informar o nome do produto, saldo em estoque, preço de venda e a previsão de rentabilidade com a venda de cada produto. Rentabilidade: Saldo em estoque * preço de venda.

l) O acesso ao sistema só pode ser feito pelo funcionário que tem permissão.

m) O sistema deve possibilitar a manutenção de dados através de funcionalidades para inclusão, alteração, exclusão e consulta. Os dados devem atender às seguintes regras:
- Código do produto deve ser único
- Nome do produto não pode estar vazio ou em branco
- Não pode ser cadastrado produto com saldo negativo
- Não pode ser cadastrado produto com saldo mínimo negativo

n) Somente uma pessoa poderá fazer o cadastro de funcionários que podem usar o sistema e bloquear o acesso caso julgue necessário.
