from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./biblioteca.db")

engine = create_engine(DATABASE_URL) # cria conexão com o banco 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Factory para criar sessões com o banco 
Base = declarative_base() # classe para nossos modelos ORM