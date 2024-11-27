SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    );
"""

SQL_INSERIR = """
    INSERT INTO categoria (nome) 
    VALUES (?);
"""

SQL_ALTERAR = """
    UPDATE categoria 
    SET nome = ?
    WHERE id = ?;
"""

SQL_EXCLUIR = """
    DELETE FROM categoria 
    WHERE id = ?;
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome
    FROM categoria 
    WHERE id = ?;
"""

SQL_OBTER_TODOS = """
    SELECT id, nome
    FROM categoria 
    ORDER BY nome;
"""