import mysql.connector

def conectar_bancodedados():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="****",
        database="sistema_3xm"
    )

    return conexao