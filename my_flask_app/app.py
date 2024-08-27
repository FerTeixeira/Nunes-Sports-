from flask import Flask  # Importa a classes Flask do pacote flask. Ela é usada para criar a instância da aplicação web
import mysql.connector   # Importa o conector MySQL para conectar ao banco de dados MySQL

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Estabelece a conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="localhost", # Especifica o host do banco de dados
    user="root", # Especifica o nome do usuário do banco de dados
    password="root",  # Especifica a senha do usuário do banco de dados
    database="WallJobs" # Nome do banco de dados que está sendo usado
)

@app.route('/') # Define a rota principal da aplicação. Quando essa URL é acessada, a função 'index' será executada.
def index():
    cursor = db.cursor() # Cria o objeto cursor que é usado para interagir com o banco de dados e executar comandos SQL.
    cursor.execute("SHOW TABLES")  # Executa o comando SQL "SHOW TABLES", que lista todas as tabelas existentes no banco de dados atual.
    tables = cursor.fetchall() # Armazena o resultado do comando "SHOW TABLES" na variável 'tables'. A função fetchall() recupera todas as linhas do resultado.
    return str(tables) # Retorna as tabelas como uma string para que sejam exibidas na página web. Isso converte o resultado (uma lista de tuplas) em uma string.

# Verifica se o script está sendo executado diretamente.
# Se for o caso, executa o servidor Flask.
if __name__ == '__main__':
    # Inicia o servidor Flask com o modo de depuração ativado.
    # O modo de depuração permite que o servidor reinicie automaticamente quando o código é modificado,
    # e também fornece um console interativo de depuração.
    app.run(debug=True)
