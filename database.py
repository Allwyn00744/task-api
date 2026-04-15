from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
DATABASE_URL="sqlite:///./task.db"
engine=create_engine(DATABASE_URL,connect_args= {"check same thread":False})
SessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine

)
Base=declarative_base()