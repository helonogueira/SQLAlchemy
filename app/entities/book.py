from pydantic import BaseModel, Field
from typing import Optional, List

class Book(BaseModel):
    """
    Entidade Book - Representa um livro na biblioteca, versão completa com relacionamentos 

    """
    id: Optional[int] = None  # Opcional, gerado pelo banco
    title: str = Field(..., min_length=1, max_length=500)  # Título obrigatório
    isbn: Optional[str] = Field(None, min_length=10, max_length=17)  # ISBN opcional
    authors: List['Author'] = Field(default_factory=list)

    class Config:
        from_attributes = True

    def __str__(self):
        return f"Book: {self.title}"

# Import no final para evitar circular import
from .author import Author
Book.model_rebuild()