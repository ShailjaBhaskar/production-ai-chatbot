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


# STEP 4 — Main chat function
def chat(query):

    # Add user message to memory
    add_user_message(query)


    # Retrieve relevant docs
    retrieved_docs = retriever.invoke(query)


    # Extract retrieved text
    context = "\n".join(
        [doc.page_content for doc in retrieved_docs]
    )


    # Extract memory text
    history = "\n".join(
        [msg.content for msg in get_chat_history()]
    )


    # Generate response
    response = chain.invoke({

        "history": history,

        "context": context,

        "question": query
    })


    # Save AI response
    add_ai_message(response)


    return response