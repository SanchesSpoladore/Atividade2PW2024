from typing import Optional, List
from models.categoria_model import CategoriaModel
from sql.categoria_sql import *
from util.db import obter_conexao


class CategoriaRepo:
    @staticmethod
    def criar_tabela():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @staticmethod
    def inserir(categoria: CategoriaModel) -> Optional[CategoriaModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_INSERIR, (categoria.nome,))
            if cursor.lastrowid:
                categoria.id = cursor.lastrowid
                return categoria
            else:
                return None

    @staticmethod
    def alterar(categoria: CategoriaModel) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_ALTERAR, (categoria.nome, categoria.id))
            return cursor.rowcount > 0

    @staticmethod
    def excluir(id_categoria: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_EXCLUIR, (id_categoria,))
            return cursor.rowcount > 0

    @staticmethod
    def obter_por_id(id_categoria: int) -> Optional[CategoriaModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_POR_ID, (id_categoria,))
            linha = cursor.fetchone()
            if linha:
                return CategoriaModel(
                    id=linha["id"],
                    nome=linha["nome"]
                )
            else:
                return None

    @staticmethod
    def obter_todos() -> List[CategoriaModel]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_TODOS)
            linhas = cursor.fetchall()
            return [
                CategoriaModel(
                    id=linha["id"],
                    nome=linha["nome"]
                ) for linha in linhas
            ]

    @staticmethod
    def inserir_categorias_iniciais():
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) AS count FROM categoria;")
            count = cursor.fetchone()["count"]
            if count > 0:
                return
            categorias_iniciais = [
                ("Fruta",), ("Verdura",), ("Tempero",), ("Legume",)
            ]
            cursor.executemany(SQL_INSERIR, categorias_iniciais)
            db.commit()
