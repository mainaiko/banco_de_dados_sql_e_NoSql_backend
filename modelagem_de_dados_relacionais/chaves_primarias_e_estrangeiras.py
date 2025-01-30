"""
Chaves primarias

identifica exclusivamente 
nao pode conter valores nulos (null)
uma tabela pode ter apenas uma chave primaria 

CREAT TABLE {{tabela}}
(ID PRIMARY KEY AUTOINCREMENT,
...)
ALTER TABLE {{tabela}}
MODIFY COLUMN ID INT PRIMARY KEY;

Chave estrnageira

ela pode ser usada para estabelecer e manter a integridade dos dados entre tabelas relacionais
ela é um atributo ou um conjunto de atributos que faz a referencia para a chave primaria
pode ser (NOT NULL); **registro orfao
é possivel ter mais de uma (ou nenhuma) em uma tabela.

CREAT TABLE {{tabela}}(
id INT PRIMARY KEY,
chave_estrangeira INT,
FOREIGN KEY (chave_estrangeira) references {{outra tabela}}(id)
);

ALTER TABLE {{tabela}}
ADD CONSTRAINT {{name_constraint}}
FOREIGN KEY (ID_)
REFERENCES {{outra_tabela}}(ID)

restriçoes:
ON DELETE especifica o que acontece com os registros dependentes quando um registro pai é excluido
ON UPDATE define o comportamento dos registros dependentes quando um registro pai é atualizado
CASCADE, SET NULL, SET DEFAULT e RESTRICT 










"""