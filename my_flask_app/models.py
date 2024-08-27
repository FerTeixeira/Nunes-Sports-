# Importa a classe SQLAlchemy do pacote Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Inicializa a instância do banco de dados
db = SQLAlchemy()


# Define a classe Produto que representa uma tabela no banco de dados
class Produto(db.Model):
    # Define a coluna 'id' como chave primária e do tipo Integer
    id = db.Column(db.Integer, primary_key=True)

    # Define a coluna 'nome' como String com um máximo de 255 caracteres e que não pode ser nula
    nome = db.Column(db.String(255), nullable=False)

    # Define a coluna 'codigo' como String com um máximo de 50 caracteres, única e não nula
    codigo = db.Column(db.String(50), unique=True, nullable=False)

    # Define a coluna 'descricao' como Texto, pode ser nula
    descricao = db.Column(db.Text)

    # Define a coluna 'preco' como do tipo Numeric com precisão 10,2 e que não pode ser nula
    preco = db.Column(db.Numeric(10, 2), nullable=False)