from typing import Optional
from fastapi import APIRouter, Form, Path, Query, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.categoria_model import CategoriaModel
from models.produto_model import ProdutoModel
from repos.categoria_repo import CategoriaRepo
from repos.produto_repo import ProdutoRepo
from util.mensagens import *


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin_produto")
def get_root(request: Request):
    produtos = ProdutoRepo.obter_todos()
    response = templates.TemplateResponse(
        "admin/index.html", {"request": request, "produtos": produtos})
    return response

@router.get("/admin_categoria")
def get_root(request: Request):
    categorias = CategoriaRepo.obter_todos()
    response = templates.TemplateResponse(
        "admin/index_categorias.html", {"request": request, "categorias": categorias})
    return response

@router.get("/admin/alterar_produto/{id}")
def get_alterar_produto(request: Request, id: int = Path(...)):
    produto = ProdutoRepo.obter_por_id(id)
    response = templates.TemplateResponse(
        "admin/alterar_produto.html", {"request": request, "produto": produto}
    )
    return response

@router.get("/admin/alterar_categoria/{id}")
def get_alterar_categoria(request: Request, id: int = Path(...)):
    categoria = CategoriaRepo.obter_por_id(id)
    if categoria:
        response = templates.TemplateResponse(
            "admin/alterar_categoria.html", {"request": request, "categoria": categoria}
        )
        return response
    else:
        response = RedirectResponse("/admin_categoria", 303)
        adicionar_mensagem_erro(response, "Categoria não encontrada!")
        return response

@router.post("/admin/alterar_produto/{id}")
def post_alterar_produto(
    request: Request, 
    id: int = Path(...),
    nome: str = Form(...),
    descricao: str = Form(...),
    estoque: int = Form(...),
    preco: float = Form(...)):
    produto = ProdutoModel(id, nome, descricao, preco, estoque)
    if ProdutoRepo.alterar(produto):
        response = RedirectResponse("/admin", 303)
        adicionar_mensagem_sucesso(response, "Produto alterado com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/alterar_produto.html", {"request": request, "produto": produto})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response
    
@router.post("/admin/alterar_categoria/{id}")
def post_alterar_categoria(
    request: Request,
    id: int = Path(...),
    nome: str = Form(...),
):
    categoria = CategoriaModel(id, nome)
    if CategoriaRepo.alterar(categoria):
        response = RedirectResponse("/admin_categoria", 303)
        adicionar_mensagem_sucesso(response, "Categoria alterada com sucesso!")
        return response
    else:
        response = templates.TemplateResponse(
            "admin/alterar_categoria.html", {"request": request, "categoria": categoria}
        )
        adicionar_mensagem_erro(response, "Não foi possível alterar a categoria!")
        return response
    
@router.get("/admin/inserir_produto")
def get_inserir_produto(request: Request):
    produto = ProdutoModel(None, None, None, None, None)
    categorias = CategoriaRepo.obter_todos()
    response = templates.TemplateResponse(
        "admin/inserir_produto.html", {"request": request, "produto": produto, "categorias": categorias}
    )
    return response

@router.get("/admin/inserir_categoria")
def get_inserir_produto(request: Request):
    categoria = CategoriaModel(None, None)
    response = templates.TemplateResponse(
        "admin/inserir_categoria.html", {"request": request, "categoria": categoria}
    )
    return response

@router.post("/admin/inserir_produto")
def post_inserir_produto(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(...),
    estoque: int = Form(...),
    preco: float = Form(...),
    categoria: Optional[int] = Form(None)
):
    produto = ProdutoModel(None, nome, descricao, preco, estoque, categoria)
    if ProdutoRepo.inserir(produto):
        response = RedirectResponse("/admin_produto", 303)
        adicionar_mensagem_sucesso(response, "Produto inserido com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/inserir_produto.html", {"request": request, "produto": produto})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response

@router.post("/admin/inserir_categoria")
def post_inserir_categoria(
    request: Request,
    nome: str = Form(...)):
    categoria = CategoriaModel(None, nome)
    if CategoriaRepo.inserir(categoria):
        response = RedirectResponse("/admin_categoria", 303)
        adicionar_mensagem_sucesso(response, "Categoria inserido com sucesso!")
        return response
    else:
        response = templates.TemplateResponse("/admin/inserir_categoria.html", {"request": request, "categoria": categoria})
        adicionar_mensagem_erro(response, "Corrija os campos e tente novamente.")
        return response
    
@router.get("/admin/excluir_produto/{id}")
def get_excluir_produto(request: Request, id: int = Path(...)):
    produto = ProdutoRepo.obter_por_id(id)
    if produto:
        response = templates.TemplateResponse(
            "admin/excluir_produto.html", {"request": request, "produto": produto}
        )
        return response
    else:
        response = RedirectResponse("/admin_produto", 303)
        adicionar_mensagem_erro(response, "O produto que você tentou excluir não existe!")
        return response
    
@router.get("/admin/excluir_categoria/{id}")
def get_excluir_categoria(request: Request, id: int = Path(...)):
    categoria = CategoriaRepo.obter_por_id(id)
    if categoria:
        response = templates.TemplateResponse(
            "admin/excluir_categoria.html", {"request": request, "categoria": categoria}
        )
        return response
    else:
        response = RedirectResponse("/admin_categoria", 303)
        adicionar_mensagem_erro(response, "A categoria que você tentou excluir não existe!")
        return response
    
@router.post("/admin/excluir_produto")
def post_excluir_produto(id: int = Form(...)):
    if ProdutoRepo.excluir(id):
        response = RedirectResponse("/admin_produto", 303)
        adicionar_mensagem_sucesso(response, "Produto excluído com sucesso!")
        return response
    else:
        response = RedirectResponse("/admin_produto", 303)
        adicionar_mensagem_erro(response, "Não foi possível excluir o produto!")
        return response
    
@router.post("/admin/excluir_categoria")
def post_excluir_categoria(id: int = Form(...)):
    if CategoriaRepo.excluir(id):
        response = RedirectResponse("/admin_categoria", 303)
        adicionar_mensagem_sucesso(response, "Categoria excluída com sucesso!")
        return response
    else:
        response = RedirectResponse("/admin_categoria", 303)
        adicionar_mensagem_erro(response, "Não foi possível excluir a categoria!")
        return response