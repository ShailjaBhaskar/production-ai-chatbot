from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.core.config import OPENAI_API_KEY

from app.services.vector_db import retriever

from app.services.memory_service import (
    add_user_message,
    add_ai_message,
    get_chat_history
)

from typing import AsyncGenerator


from app.services.db_memory_service import (
    save_message,
    get_history
)


# STEP 1 — Create LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    streaming=True
)


async def stream_chat(query: str) -> AsyncGenerator[str, None]:

    async for chunk in llm.astream(query):

        content = chunk.content

        if content:

            yield str(content)

# STEP 2 — Prompt Template
prompt = PromptTemplate(

    input_variables=[
        "history",
        "context",
        "question"
    ],

    template="""
You are a helpful AI assistant.

Answer the user's question ONLY using the retrieved context below.

If the answer is not present in the context, say:
"I could not find the answer in the provided context."

Conversation History:
{history}

Retrieved Context:
{context}

User Question:
{question}
"""
)


# STEP 3 — Create chain
chain = prompt | llm | StrOutputParser()


# # STEP 4 — Main chat function
# def chat(query):

#     # Add user message to memory
#     add_user_message(query)


#     # Retrieve relevant docs
#     retrieved_docs = retriever.invoke(query)


#     # Extract retrieved text
#     context = "\n".join(
#         [doc.page_content for doc in retrieved_docs]
#     )


#     # Extract memory text
#     history = "\n".join(
#         [msg.content for msg in get_chat_history()]
#     )


#     # Generate response
#     response = chain.invoke({

#         "history": history,

#         "context": context,

#         "question": query
#     })


#     # Save AI response
#     add_ai_message(response)


#     return response


def chat(user_id, query):


    # STEP 1 — Save user message
    save_message(
        user_id,
        "user",
        query
    )


    # STEP 2 — Retrieve relevant docs
    retrieved_docs = retriever.invoke(query)


    # STEP 3 — Build context
    context = "\n".join(
        [doc.page_content for doc in retrieved_docs]
    )


    # STEP 4 — Get user conversation history
    messages = get_history(user_id)


    # STEP 5 — Convert history to text
    history = "\n".join(
        [
            f"{msg.role}: {msg.content}"
            for msg in messages
        ]
    )


    # STEP 6 — Generate AI response
    response = chain.invoke({

        "history": history,

        "context": context,

        "question": query
    })


    # STEP 7 — Save AI response
    save_message(
        user_id,
        "assistant",
        response
    )


    return response