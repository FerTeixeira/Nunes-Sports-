from flask import Flask, request, jsonify  # Importa as classes Flask, request e jsonify do pacote flask. Flask é usado para criar a instância da aplicação web, request para manipular solicitações HTTP e jsonify para converter dados em JSON.
import mysql.connector   # Importa o conector MySQL para conectar ao banco de dados MySQL
from models import db, Produto  # Importa a instância db e o modelo Produto de um módulo separado, geralmente para configurar o banco de dados e definir modelos de dados
from config import Config  # Importa a classe Config do módulo config para carregar configurações

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Configura a aplicação Flask com as configurações definidas na classe Config
app.config.from_object(Config)

# Inicializa a conexão com o banco de dados, configurado em models.py
db.init_app(app)

# Estabelece a conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="localhost", # Especifica o host do banco de dados
    user="root", # Especifica o nome do usuário do banco de dados
    password="root",  # Especifica a senha do usuário do banco de dados
    database="WallJobs" # Nome do banco de dados que está sendo usado
)

@app.before_first_request
def create_tables():
    # Cria todas as tabelas definidas nos modelos antes do primeiro pedido ser tratado
    db.create_all()

@app.route('/') # Define a rota principal da aplicação. Quando essa URL é acessada, a função 'index' será executada.
def index():
    cursor = db.cursor() # Cria o objeto cursor que é usado para interagir com o banco de dados e executar comandos SQL.
    cursor.execute("SHOW TABLES")  # Executa o comando SQL "SHOW TABLES", que lista todas as tabelas existentes no banco de dados atual.
    tables = cursor.fetchall() # Armazena o resultado do comando "SHOW TABLES" na variável 'tables'. A função fetchall() recupera todas as linhas do resultado.
    return str(tables) # Retorna as tabelas como uma string para que sejam exibidas na página web. Isso converte o resultado (uma lista de tuplas) em uma string.

@app.route('/produtos', methods=['POST'])  # Define a rota para criar um novo produto usando o método POST
def create_produto():
    data = request.json  # Obtém os dados JSON da solicitação
    novo_produto = Produto(
        nome=data['nome'],  # Define o nome do produto
        codigo=data['codigo'],  # Define o código do produto
        descricao=data.get('descricao'),  # Define a descrição do produto, se fornecida
        preco=data['preco']  # Define o preço do produto
    )
    db.session.add(novo_produto)  # Adiciona o novo produto à sessão do banco de dados
    db.session.commit()  # Confirma a transação no banco de dados
    return jsonify({'id': novo_produto.id}), 201  # Retorna o ID do novo produto e o status HTTP 201 (Criado)

@app.route('/produtos', methods=['GET'])  # Define a rota para obter todos os produtos usando o método GET
def get_produtos():
    produtos = Produto.query.all()  # Obtém todos os produtos da tabela
    resultado = [
        {
            'id': produto.id,  # ID do produto
            'nome': produto.nome,  # Nome do produto
            'codigo': produto.codigo,  # Código do produto
            'descricao': produto.descricao,  # Descrição do produto
            'preco': str(produto.preco)  # Preço do produto convertido para string
        }
        for produto in produtos
    ]
    return jsonify(resultado)  # Retorna a lista de produtos em formato JSON

@app.route('/produtos/<int:id>', methods=['PUT'])  # Define a rota para atualizar um produto específico usando o método PUT
def update_produto(id):
    data = request.json  # Obtém os dados JSON da solicitação
    produto = Produto.query.get_or_404(id)  # Obtém o produto com o ID fornecido ou retorna um erro 404 se não encontrado
    produto.nome = data.get('nome', produto.nome)  # Atualiza o nome do produto, se fornecido
    produto.codigo = data.get('codigo', produto.codigo)  # Atualiza o código do produto, se fornecido
    produto.descricao = data.get('descricao', produto.descricao)  # Atualiza a descrição do produto, se fornecida
    produto.preco = data.get('preco', produto.preco)  # Atualiza o preço do produto, se fornecido
    db.session.commit()  # Confirma a transação no banco de dados
    return jsonify({
        'id': produto.id,  # ID do produto atualizado
        'nome': produto.nome,  # Nome do produto atualizado
        'codigo': produto.codigo,  # Código do produto atualizado
        'descricao': produto.descricao,  # Descrição do produto atualizada
        'preco': str(produto.preco)  # Preço do produto atualizado convertido para string
    })

@app.route('/produtos/<int:id>', methods=['DELETE'])  # Define a rota para deletar um produto específico usando o método DELETE
def delete_produto(id):
    produto = Produto.query.get_or_404(id)  # Obtém o produto com o ID fornecido ou retorna um erro 404 se não encontrado
    db.session.delete(produto)  # Remove o produto da sessão do banco de dados
    db.session.commit()  # Confirma a transação no banco de dados
    return '', 204  # Retorna um status HTTP 204 (Sem Conteúdo) indicando que a operação foi bem-sucedida



# Verifica se o script está sendo executado diretamente.
# Se for o caso, executa o servidor Flask.
if __name__ == '__main__':
    # Inicia o servidor Flask com o modo de depuração ativado.
    # O modo de depuração permite que o servidor reinicie automaticamente quando o código é modificado,
    # e também fornece um console interativo de depuração.
    app.run(debug=True)
