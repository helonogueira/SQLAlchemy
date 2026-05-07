from pydantic import BaseModel, EmailStr, Field 
# Classe base do Pydantic, traz validação automática e serialização;
# Tipo especial para validar e garantir formato de email;
# Permite definir regras extras para os campos (obrigatoriedade, tamanho, etc).
from typing import Optional, List
#  Optional indica que o campo pode ser None (opcional).

class Author(BaseModel): # Herda de BaseModel, tornando a classe uma entidade Pydantic.
    """
    Entidade Author - Representa um autor de livros

    """
    id: Optional[int] = None  # Identificador do autor, opcional pois geralmente é gerado pelo banco.
    name: str = Field(..., min_length=1, max_length=255) # Nome obrigatório, entre 1 e 255 caracteres.
    email: EmailStr # Email obrigatório, validado automaticamente.
    books: List['Book'] = Field(default_factory = list)
    #           ↑ String quote porque Book ainda não foi definido
    #                           ↑ Cria uma nova lista para cada instância

    class Config:
        from_attributes = True # Permite converter objetos SQLAlchemy para Pydantic facilmente.

    def __str__(self):
        return f"Author: {self.name} ({self.email})"

# Import no final para evitar circular import
from .book import Book
Author.model_rebuild()
# ↑ Necessário para resolver as referências circulares

# Resumo: Essa estrutura garante que todo autor criado seja válido, com nome preenchido e email correto, além de facilitar integração com banco e APIs.