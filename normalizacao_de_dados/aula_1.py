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



"""