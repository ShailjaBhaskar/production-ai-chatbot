from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# STEP 1 — Database URL
DATABASE_URL = "sqlite:///chatbot.db"


# STEP 2 — Create engine
engine = create_engine(DATABASE_URL)


# STEP 3 — Create session factory
SessionLocal = sessionmaker(bind=engine)


# STEP 4 — Base class
Base = declarative_base()