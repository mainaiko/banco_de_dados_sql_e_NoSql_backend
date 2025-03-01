"""
igualdade
realizar consultas baseadas em um valor especifico para um campo
db.usuarios.find({"endereco.cidade": "sao paulo"})

operadores logicos
ralizar consultas baseadas em um valor especifico para um campo
$and
$or
$not

operadores de comparaçao
(esquerda mongo direita python)
$ep: ==
$ne: !=
$gt: >
$gte: >=
$it: <
$ite: <=
$in: []
$nin: [] negaçao

projeçoes
definir quais campos devem ser retornados em uma consulta

ordenaçao
ordenar os resultados de uma consulta com base em um ou mais campos

limitaçao
limitar o numero de documentos retornados em uma consulta

paginaçao
db.usuarios.find().skip(10).limit(5)

ex de uso:

{cidade: ($in:["Sao paulo","belo horizonte"])}

project {nome: 1}
sort {idade: 1, nome: -1}
limit {1}

ou

db.usuarios.find({cidade: {$nin:["Sao paulo"]}}, {nome: 1}).sort({idade:1}).limit(1)
"""