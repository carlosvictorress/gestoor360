import os
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env
load_dotenv()

# Tenta ler a variável DATABASE_URL
database_url = os.environ.get("DATABASE_URL")

print("--- Teste de Leitura do Ficheiro .env ---")
if database_url:
    print(f"SUCESSO: A variável foi encontrada!")
    print(f"DATABASE_URL = {database_url}")
else:
    print("FALHA: A variável DATABASE_URL não foi encontrada no ambiente.")
print("-----------------------------------------")
