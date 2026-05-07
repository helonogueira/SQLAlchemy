from sqlalchemy.orm import Session
from models.loan_model import LoanModel
from repositories.base_repository import BaseRepository

class LoanRepository(BaseRepository[LoanModel]):
    def __init__(self, session: Session):
        super().__init__(session, LoanModel)

    def get_by_user(self, user_name: str) -> list[LoanModel]:
        """Busca empréstimos por usuário (busca parcial)"""
        return self.session.query(LoanModel).filter(LoanModel.user_name.ilike(f"%{user_name}%")).all()

    def get_active_loans(self) -> list[LoanModel]:
        """Busca empréstimos ainda não devolvidos"""
        return self.session.query(LoanModel).filter(LoanModel.returned == False).all()

    def get_by_book(self, book_id: int) -> list[LoanModel]:
        """Busca empréstimos de um livro específico"""
        return self.session.query(LoanModel).filter(LoanModel.book_id == book_id).all()