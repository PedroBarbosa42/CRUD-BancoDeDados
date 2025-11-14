import sqlite3

conexao = sqlite3.connect("Banco.db")

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE Produto (
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            preco DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
            estoque INT NOT NULL DEFAULT 0  

);
    '''
)

cursor.close()
print("Tabela Produto criada com sucesso!")
