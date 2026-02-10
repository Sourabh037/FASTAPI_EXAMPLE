from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_models import Base

db_url = "mysql://root:DoOm_07_SsB@localhost:3306/telusko"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush = False, bind = engine)