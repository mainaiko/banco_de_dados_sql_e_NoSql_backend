"""
indices de busca
analise do plano de execuçao
ela nos permite examinar as operaçoes realizadas, as tabelas acessadas. os indices utilizados
e outras informaçoes importantes para identificar possiveis melhorias de desempenho

EXPLAIN
    SELECT *
    FROM {{TABELA}}

analise do plano de execuçao
select_type: "SIMPLE", "SUBQUERY", "JOIN"
table.
type: "ALL", "INDEX" entre outros
possible_keys: os indices possiveis que podem ser utilizados na operaçao
key: o indice utilizado na operaçao se aplicavel
key_len: o comprimento do indice utilizado
ref: as colunas ou constantes usadas para acessar o indice rows
"""