"""
tabelas:
ela é usada para armazenar dados de forma organizada. cada tabela em um banco de dados relacional
tem um nome unico e é dividida em colunas e linhas

colunas:
uma coluna é uma estrutura dentro de uma tabela que representa uma atributo especifico dos dados armazenados
cada coluna tem um nome unico e um tipo de dados associado que define o tipo de informaçao que pode ser armazenado nela
como numeros, textos, datas e etc.

registros:
um registro, tambem conhecido como linha ou tupla é uma instancia de dados em uma tabela


comando: 
creat table{{nome}}
    ({{coluna}}{{tipo}}{{opçoes}} comment {{'comentario'}})

opçoes:
restriçoes de valor
    not null
    unique
    default
chaves primarias e estrangeiras
auto incremento

tipos de dados
os dados podem variar muito entre diversos SGBD, os mais comuns sao:

inteiro (iteger)
decimal/numerico (decimal/numeric)
caractere/varchar (character/ varchar)
data/hora (date/tine)
booleano (boolean)
texto longo (text)

comando:
select{{lista_colunas}}
from tabela

operadores select:
=
<> !=
<
>
>=
<=
like (comparaçao de padroes)
in (pertence a uma lista de valores)
between (dentro de um intervalo)
and
or






"""