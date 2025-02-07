"""
Junçoes conhecidas como JOINs:
Sao usadas no SQL para combinar dados de duas ou mais tabelas relacionadas em uma unica consualta
junçoes:tipos
INNER JOIN
LEFT JOIN ou LEFT OUTER JOIN
RIGHT JOIN ou RIGHT OUTER JOIN
FULL JOIN ou FULL OUTER JOIN

__INNER JOIN__
retorna apenas as linhas que tem correspondencia em ambas as tabelas envolvidas na junçao. A junçao é feita
com base em uma condiçao de igualdade especificada na clausula ON

    SELECT*
    FROM tabela1
    INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna

__LEFT JOIN__
retorna todas as linhas da tabela a esquerda da junçao e as linhas correspondentes da tabela a direita. se nao houver
correspondencia, os valores da tabela a direita serao NULL

    SELECT*
    FROM tabela1
    LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

__RIGHT JOIN__
retorna todas as linhas da tabela a direita da junçao e as linhas correspondentes da tabela a esquerda. se nao houver
correspondencia, os valores da tabela a esquerda serao NULL

    SELECT*
    FROM tabela1
    RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

__FULL JOIN__
retorna todas as linhas de ambas as tabelas envolvidas na junçao, combinanco-as com base em uma condiçao de igualdade.
se nao houver correspondencia, os valores ausentes serao preenchidos com NULL

    SELECT*
    FROM tabela1
    FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna;

Sub consultas ou consultas aninhadas
elas permitem realizar consultas mais complexas permitindo que voce use o resultado de uma consulta como entrada para
outra consulta
as subconsultas podem ser usadas em varias partes de uma consulta
SELECT
FROM
WHERE
HAVING
JOIN





"""