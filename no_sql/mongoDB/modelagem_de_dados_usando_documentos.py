"""
estrutura do mongodb

data_base
    coleçao(documentos)
    coleçao2(documentos)

coleçoes:
agrupamento logico de documentos
nao exige esquema ou que os documentos tenham a mesma estrutura
    caracteristicas:
    devem começar com uma letra ou um underscore(_)
    podem conter letras numeros e underscores
    nao podem ser vazios
    nao podem ter mais de 64bytes de comprimento

documentos:
sao armazenados em documentos BSON(binary JSON) que sao estruturas flexiveis e semiestruturadas
cada documento possui um identificador unico chamado "_id"
é composto por pares de chave e valores
    caracteriticas:
    tamanho maximo de no maximo 16mb
    aninhammento de documentos
    flexibilidade na evoluçao do esquema
    tipos de dados simples:
    string
    number
    boolean
    date
    null
    objectld
    tipos de dados complexos:
    array
    documento embutido
    referencia
    geoJSON
estrutura de um documento

{
    _id:ObjectId(""),
    "nome_campo":"valor_campo",
    ...
}
"""

"""
modelagem do usuario:
{
"_id": 1,
"nome": "Aiko Marques",
"idade": 24,
"data_nascimento": "2001-05-01",
"endereco": "raiacho 2",
"enderecos":[{
"logradouro": "riacho 2",
"numero": 5,
"bairro": "qc02",
"cidade": "brasilia"
}],
"interesses": ["verde", "agua", "paz"],
"reservas": [ ObjectId("123"), ObjectId("456") 
]
}
"""
"""
modelagem do destino:
{
"_id": 2,
"nome": "Chapada dos veadeiros",
"descricao": "bao dimais",
"localizacao": {
"type": "Point",
"coordinates": [-14.046000, -47.395999]
}
}
"""
"""
modelagem referencia
{
"_id": ObjetctId("123"),
"destino": ObjetctId("456"),
"data": "2025-02-15",
"status": "pendente",
"usuario": ObjectId(345),
}

"""