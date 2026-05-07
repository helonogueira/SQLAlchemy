from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Loan(BaseModel):
    """
    Entidade Loan - Representa um empréstimo de livro
    """
    id: Optional[int] = None  # Opcional, gerado pelo banco
    book_id: int  # ID do livro emprestado, obrigatório
    user_name: str = Field(..., min_length=1, max_length=255)  # Nome do usuário, obrigatório
    loan_date: date  # Data do empréstimo
    return_date: Optional[date] = None  # Data de devolução, opcional
    returned: bool = False  # Se o livro foi devolvido, padrão False

    class Config:
        from_attributes = True

    def __str__(self):
        return f"Loan: {self.user_name} - Book ID: {self.book_id} ({'Devolvido' if self.returned else 'Em aberto'})"