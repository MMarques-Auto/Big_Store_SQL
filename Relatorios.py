import sqlite3
import pandas

conexao = sqlite3.connect('ecommerce.db')
cursor = conexao.cursor()

cursor.execute("SELECT SUM(valor) FROM vendas")
somavenda = cursor.fetchone()[0]
print(f"TOTAL de vendas: {somavenda:,.2f}\n")

cursor.execute("SELECT cliente, COUNT(*) as total_vendas FROM vendas GROUP BY cliente ORDER BY total_vendas DESC LIMIT 3")
top3 = cursor.fetchall()
print(f"Maiores compradores de hoje:\n")
for cliente in top3:
    print(f"  - {cliente[0]} comprou {cliente[1]} vezes")
print("")

cursor.execute("SELECT * FROM vendas WHERE valor>3000 ORDER BY valor DESC LIMIT 10")
gastoalto = cursor.fetchall()
print(f"Vendas +3000,00 hoje:")
for vendas in gastoalto:
    print(f"   - {vendas[1]} | R$ {vendas[2]:,.2f} | Cliente: {vendas[3]}")

conexao.close()