from app.services.db_memory_service import (
    save_message,
    get_history
)


save_message(
    "shailja",
    "user",
    "Hello AI"
)


messages = get_history("shailja")


for msg in messages:

    print(msg.role, ":", msg.content)