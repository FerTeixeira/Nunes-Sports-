# Importa o módulo 'os' para acessar variáveis de ambiente
import os


# Define uma classe de configuração para o Flask
class Config:
    # Define a URI de conexão com o banco de dados usando uma variável de ambiente.
    # Se a variável de ambiente 'DATABASE_URL' não estiver definida, usa a URI padrão fornecida.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:root@WallJobs/nunes_sports')

    # Desativa a modificação de rastreamento de objetos, o que pode ajudar a economizar memória.
    # Esta configuração é opcional e pode melhorar o desempenho, especialmente em grandes aplicações.
    SQLALCHEMY_TRACK_MODIFICATIONS = False