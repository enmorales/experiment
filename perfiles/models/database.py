from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:5mG$1**8abcd@abc-jobs-postgres.cy4wad57lz7h.us-east-1.rds.amazonaws.com:5432/postgres'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()