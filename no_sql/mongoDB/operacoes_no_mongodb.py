"""
Criando um dataBase
use{{nome_do_banco}}

enquanto o database nao tiver uma collection ele nao sera apresentado na lista

Criando uma collection

db.createCollection("usuarios")
db.createCollection("destinos")

Inserindo documentos

db.usuarios.insertOne({});
db.usuarios.insertMany([{}]);

consultando documentos

db.usuarios.find({})
db.usuarios.findOne({})
db.usuarios.findOneAndUpdate({})
db.usuarios.findOneAndDelete({})

Excluindo documentos

db.usuarios.deleteOne({});
db.usuarios.deleteMany({});
"""