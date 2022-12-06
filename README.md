# Vamos alterar bancos de dados criados em SQL usando um script feito em Python 3

Este projeto ilustra como podemos fazer CRUD (Create, Read, Update, Delete) em arquivos .sql , usando spftwares Python para isto. Isto é particularmente util se você precisar inserir (ex:) informações de login em uma página de internet feita em Flask Framework ou similares usando Pytrhon.

#### Você precisa ter o Mysql instalado na sua máquina.

#### Você pode começar testando se sua instalação do Mysql esta funcionando, criando um banco e uma tabela:


-> Abra o prompt de comandos e digite:

$ mysql -u Seu_Usuario -p



-> Logando no Mysql crie um Banco e uma tabela com duas colunas:

CREATE DATABASE DB_01;
show databases;
use DB_01;
select * from DB_01;

CREATE TABLE  Venda( nome_produto varchar(30) not NULL,
valor varchar(30) not null);




-> Estando tudo em ordem, podemos rodar o Script em Python.
