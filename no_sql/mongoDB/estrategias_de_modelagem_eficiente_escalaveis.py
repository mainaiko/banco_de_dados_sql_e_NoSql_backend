"""
Modelagem orientada por consultas
a modelagem de dados no mongod deve ser orientada pelas consultas que serao realizadas com mais frequencia

Inner documents
no mongodb, é comum denormalizar os dados para evitar operaçoes de junçao (join) custosas. isso significa que os
dados relacionados podem ser armazenados juntos em um unico documento, em vez de serem distribuidos em varias coleçoes
    quando usar
    os dados aninhados sao especificos para o documento pai
    os dados aninhados sao sempre acessados juntamente com o documento pai
    a cardinalidade do realacionamento é um-para-muitos(um usuario pode ter varias reservas)
    quando nao usar
    se os dados aninhados precisarem ser consultados e atualizados idenpendente do documento pai, é mais adequado usar
    as coleçoes separadas

Modelar usuario com estrategia de referencia
    quando usar
    os dados tem seu proprio significado e podem ser acessados idenpendentemente do documento pai
    os dados tem uma cardinalidade mais alta(ex, varios usuarios poderm ter reservas)
    quando nao usar
    se os dados aninhados precisarem ser consultados e atualizados idenpendentemente do documento pai, é mais adequado utilizar
    coleçoes separadas
"""