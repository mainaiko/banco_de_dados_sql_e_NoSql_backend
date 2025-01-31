"""
problema:
1   |Kamille   |rua x, 123, cidade y, estado z
2   |Aiko   |rua x, 456, cidade a, estado z
3   |Fatima   |rua x, 789, cidade y, estado z

como procuarar todos os usuarios da cidade y?

A normalizaçao de dados é um processo no qual se organiza e estrutura um banco de dados relacional de 
forma a eliminar as redundancias e anomalias, garantindo a consistencia e integridade dos dados

fORMAS NORMAIS:
1 forma normal: atomicidade de dados
a 1fn estabelece que cada valor em uma tabela deve ser atomico, ou seja, indivisivel. nenhum campo deve 
conter multiplos valores ou listas. No seu caso, o campo "endereco" contem multiplos valores, como rua,
numero, cidade e estado. para garantir a 1fn, precisamos dividir o campo "endereco" em colunas separadas

2 forma normal:
a 2fn estabelece que uma tabela deve estar na 1fn
todos os atributos nao chave devem depender totalmente da chave primaria
Dica* se sua tabela tem uma chave primaria simples nao existe a possibilidade de termos dependencia parcial
e por tanto ela se encontra na 2fn

3 forma normal:
uma tabela deve estar na 2fn
nehuma coluna nao chave depender de outra coluna nao chave
nosso exemplo: realaçao estado -> cidade

__RESUMO__
A 1fn garante que cada valor seja atomico e que seus registros sejam unicos e identificaveis
A 2fn garante que os atributos chave dependam totalmente da chave primaria, evitando dependencias parciais
A 3fn elimina dependecias transitivas entre os atributos nao chave, garantindo que cada atributo nao chave dependa
apenas da chave primaria, nao havendo dependencias indiretas entre eles


""" 