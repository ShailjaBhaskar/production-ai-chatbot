from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from app.core.config import OPENAI_API_KEY
from app.services.documents import documents


# STEP 1 — Create embedding model
embedding_model = OpenAIEmbeddings(
    api_key=OPENAI_API_KEY,
    model="text-embedding-3-small"
)


# STEP 2 — Create vector store
vector_store = Chroma.from_texts(
    texts=documents,
    embedding=embedding_model
)


# STEP 3 — Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)