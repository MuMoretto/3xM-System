from sql_bd import conectar_bancodedados

conn = conectar_bancodedados()

print("Conexão com Banco de Dados completa...")

conn.close()