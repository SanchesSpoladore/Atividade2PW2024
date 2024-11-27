from dataclasses import dataclass
from typing import Optional


@dataclass
class CategoriaModel:
    id: Optional[int] = None
    nome: Optional[str] = None