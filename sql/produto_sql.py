SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);
"""

SQL_INSERIR = """
INSERT INTO produto (nome, descricao, preco, estoque, categoria_id) 
VALUES (?, ?, ?, ?, ?);
"""

SQL_ALTERAR = """
UPDATE produto 
SET nome = ?, descricao = ?, preco = ?, estoque = ?, categoria_id = ? 
WHERE id = ?;
"""

SQL_EXCLUIR = """
DELETE FROM produto WHERE id = ?;
"""

SQL_OBTER_POR_ID = """
SELECT id, nome, descricao, preco, estoque, categoria_id 
FROM produto 
WHERE id = ?;
"""

SQL_OBTER_TODOS = """
SELECT id, nome, descricao, preco, estoque, categoria_id 
FROM produto;
"""
