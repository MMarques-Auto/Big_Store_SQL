import sqlite3
import random

conexao = sqlite3.connect('ecommerce.db')
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS vendas")
cursor.execute("""
CREATE TABLE vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT,
    valor REAL,
    cliente TEXT
)
""")

produtos = ['RTX 4060', 'Ryzen 7', 'Memória RAM 16GB', 'SSD 1TB', 'Gabinete Mesh']
clientes = ['Murilo', 'Ana', 'Beto', 'Carla', 'Diego', 'Elena']

print("Criando banco...")

for i in range(100):
    prod = random.choice(produtos)
    val = round(random.uniform(200.0, 4500.0), 2)
    cli = random.choice(clientes)
    cursor.execute(f"INSERT INTO vendas (produto, valor, cliente) VALUES ('{prod}', {val}, '{cli}')")

conexao.commit()
conexao.close()
print("DB criado, lembre de verificar com SQL Viewer")