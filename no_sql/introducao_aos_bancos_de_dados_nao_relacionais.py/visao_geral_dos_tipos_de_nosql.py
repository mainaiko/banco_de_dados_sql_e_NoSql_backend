"""
Tipos
key-value
documento
coluna
grafos
entre outros...

key-value > chave valor
armazena dados como pares de chave e valor, onde cada chave é um identificador unico para acessar
o valor correspondente
Ex de sgbd: redis, riak, amazon dynamoDB
uso: um site pode usar um banco de dados redis para armazenar informaçoes de sessao de usuario

document > documento
armazena dados em documentos semiestruturados geralmente em formato JSON ou BSON
Ex de sgbd: mongoDB, couchbase, apache couchDB
uso: um catalogo de e-commerce pode usar o mongoDB para armazenar informaçoes de produtos como nome, 
descriçao, preço e atributos adicionais

coluna
armazena dados em formato de coluna, o que permite alta escalabilidade e eficiencia em determinados tipos
de consultas
Ex de sgdb: apache cassandra, scryllaDB, HBase
uso: um sistema de registro de aplicativos pode usar o apache cassandra para armazenar registros de log



"""