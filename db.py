from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

# url = URL(
#     drivername="postgresql",
#     username="postgres",
#     password="postgres",
#     host="localhost",
#     database="postgres",
#     port=5432,
# )

url = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(url)
Session = sessionmaker(bind= engine)
session = Session()