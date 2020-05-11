[![Build Status](https://travis-ci.org/RamiroAlvaro/desafio-nivel-2.svg?branch=master)](https://travis-ci.org/RamiroAlvaro/desafio-nivel-2)

# Desafio nível 2
A idéia deste desafio é nos permitir avaliar melhor as habilidades de candidatos à vagas de desenvolvedor, de vários níveis.

Este desafio deve ser feito por você em sua casa. Gaste o tempo que você quiser, porém normalmente você não deve precisar de mais do que algumas horas.

## Instruções de entrega do desafio
1. Primeiro, faça um fork deste projeto para sua conta no Github (crie uma se você não possuir).
1. Em seguida, implemente o projeto tal qual descrito abaixo, em seu próprio fork.
1. Por fim, empurre todas as suas alterações para o seu fork no Github e envie um pull request para este repositório original. Se você já entrou em contato com alguém da Garage Geek sobre uma vaga, avise também essa pessoa por email, incluindo no email o seu usuário no Github.

## Instruções alternativas de entrega do desafio (caso você não queira que sua submissão seja pública)
1. Faça um clone deste repositório.
1. Em seguida, implemente o projeto tal qual descrito abaixo, em seu clone local.
1. Por fim, envie via email um arquivo patch para seu contato na Garage Geek.

## Descrição do projeto

Desenvolver um sistema para cadastrar estados e cidades Brasileiras.

Sua tarefa é criar uma interface web que aceite o cadastro de estados e cidades Brasileiras, normalize os dados e armazene-os em um banco de dados relacional.

Sua aplicação web DEVE:

1. Aceitar (via um formulário e via API) o cadastro de estados
1. Aceitar (via um formulário e via API) o cadastro de cidades
1. Listar todas as cidades e estados cadastrados
1. Ser escrita obrigatoriamente em Ruby 2.0+, Python 3.6+, Java 7+ ou PHP 5.3+ (caso esteja entrevistando para uma vaga específica, utilize a linguagem solicitada pela vaga).
1. Ser simples de configurar e rodar, funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.

Sua aplicação web não precisa:

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
1. Ser escrita usando algum framework específico (mas não há nada errado em usá-los também, use o que achar melhor).
1. Ter uma aparência bonita.

## Avaliação
Seu projeto será avaliado de acordo com os seguintes critérios.

1. Sua aplicação preenche os requerimentos básicos?
1. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
1. Você seguiu as instruções de envio do desafio?
1. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.8
3. Ative o virtualenv.
4. Instale as dependências.
5. Execute o servidor de banco de dados Postgres.
6. Crie o banco de dados e preencha-o com dados de amostra.
7. Execute os testes.
8. Execute o aplicativo.

```console
git clone git@github.com:RamiroAlvaro/desafio-nivel-2.git desafio-nivel-2
cd desafio-nivel-2
python3 -m venv .env
source .env/bin/activate
pip install -r requirements-dev.txt
docker run --rm -it -p 5432:5432 postgres:10
python init_db.py
cd aiohttp_desafio
pytest tests
cd ..
python3 -m aiohttp_desafio
```
## URLs API

![GET /api](images/api_1.png)

![GET /api/1](images/api_2.png)

![POST /api/state](images/api_3.png)

![POST /api/city](images/api_4.png)
