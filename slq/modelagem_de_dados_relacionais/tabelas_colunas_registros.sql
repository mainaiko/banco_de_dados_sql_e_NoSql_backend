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

ALTER TABLE usuarios
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

ALTER TABLE usuarios
ADD CONSTRAINT opa_testes
FOREING KEY (id_usuario) REFERENCES usuarios(id);

 
ALTER TABLE usuarios
ADD rua VARCHAR (100),
ADD numero VARCHAR (10), 
ADD cidade VARCHAR (50),
ADD estado VARCHAR(20);

UPDATE usuarios
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1)
    numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1)
    cidade = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1)
    estado = SUBSTRING_INDEX(endereco, ',', 1);

ALTER TABLE usaurios
DROP COLUMN endereco;

SELECT * FROM usuarios us
INNER JOIN  reservas rs ON us.id = rs.id_usuario
INNER JOIN destinos ds ON rs.id_destino = ds.id;

INSERT INTO usuarios(nome, email, data_nascimento, numero, cidade, estado) VALUES
("sem reservas", "pipipopopo@gmail", "01/08/750", "05", "xique-xique", "bahia");

SELECT * FROM usuarios us
INNER JOIN reservas rs ON us.id = rs.id_usuario;

SELECT * FROM usuarios us
LEFT JOIN reservas rs ON us.id = rs.id_usuario;

SELECT * FROM reservas;

SELECT * FROM destinos;

INSERT INTO destinos (nome, descricao) VALUES
("destino teste", "lugazin bao em")

SELECT * FROM destinos;

SELECT * FROM reservas rs
RIGHT JOIN destinos ds ON rs.id_destino = ds.id

SELECT * FROM destinos
WHERE id NOT IN (SELECT id_destino FROM reservas);

SELECT COUNT(*) FROM usuarios;

SELECT COUNT(*) AS total_usuarios FROM usuarios us
INNER JOIN reservas rs ON us.id = rs.id;

SELECT MAX(TIMESTANPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS maior_idade
FROM usuarios;

INSERT INTO reservas(id_usuario, id_destino) VALUES (1,1);

SELECT * FROM reservas;

SELECT COUNT(*) AS qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas;

CREAT INDEX idx_name ON usuarios (nome);





