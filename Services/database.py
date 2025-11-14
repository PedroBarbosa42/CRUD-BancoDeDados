import sqlite3

server = ''
username = ''
password = ''
database = 'Banco.db'
conexão = sqlite3.connect(database)
print("Banco de Dados criado com sucesso!")