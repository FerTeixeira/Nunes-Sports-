import mysql.connector

db = mysql.connector.connect(
    host="localhost", # Especifica o host do banco de dados
    user="root", # Especifica o nome do usuário do banco de dados
    password="root",  # Especifica a senha do usuário do banco de dados
    database="WallJobs" # Nome do banco de dados que está sendo usado
)

cursor = db.cursor()

# Executar comandos SQL
cursor.execute("SHOW TABLES")

# Exibir as tabelas
for table in cursor:
    print(table)

# Fechar a conexão
db.close()