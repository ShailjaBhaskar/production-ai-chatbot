from app.core.database import engine
from app.models.chat_models import Base


Base.metadata.create_all(bind=engine)

print("Database tables created")