from app.core.database import SessionLocal

from app.models.chat_models import Message


# STEP 1 — Save message
def save_message(user_id, role, content):

    db = SessionLocal()


    message = Message(
        user_id=user_id,
        role=role,
        content=content
    )


    db.add(message)

    db.commit()

    db.close()


# STEP 2 — Get user-specific history
def get_history(user_id):

    db = SessionLocal()


    messages = db.query(Message).filter(
        Message.user_id == user_id
    ).all()


    db.close()

    return messages