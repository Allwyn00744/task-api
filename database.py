from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
Database_URL="sqlite:///./task.db"
engine=create_engine(Database_URL)
sessionLocal=sessionmaker(bind=engine)
base=declarative_base()