INSERT INTO usuarios (id, nome, email, data_nascimento, endereco) VALUES (1, "aiko", "aiko58912@gmail.com", "05/01/2001", "QC02 conj4")

INSERT INTO destinos (id, nome, descricao) VALUES (2, "praia", "lugazin bao")

INSERT INTO reservas (id, id.usuarios, id.destinos, status, data) VALUES (3, 1, 2, "pendente", "04/2025")

SELECT * FROM usuarios;

UPDATE  usuarios
SET id = 1
WHERE email = "teste@gmail.com"

DELETE FROM destino
WHERE nome = "praia do rosa"

INSERT INTO usuarios (id, nome, email, data_nascimento, endereco)
SELECT id, nome, email, data_nascimento, endereco
FROM usuarios;

SELECT * FROM usuarios_nova;

DROP TABLE usuarios;

ALTER TABLE usuarios_nova RENAME usuarios;

ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR (150);




