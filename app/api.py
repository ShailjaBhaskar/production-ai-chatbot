# from fastapi import FastAPI

# from app.models.request_models import QueryRequest

# from app.services.chatbot_service import chat


# app = FastAPI()


# @app.post("/chat")
# def chat_endpoint(request: QueryRequest):

#     response = chat(request.query)

#     return {
#         "response": response
#     }

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.services.chatbot_service import stream_chat
from app.models.request_models import QueryRequest
from app.services.chatbot_service import chat

import asyncio


app = FastAPI()


async def fake_ai_stream():

    words = [
        "Hello",
        "this",
        "is",
        "streaming",
        "response"
    ]


    for word in words:

        yield word + " "

        await asyncio.sleep(0.5)


@app.get("/stream")
async def stream_response():

    return StreamingResponse(
        fake_ai_stream(),
        media_type="text/plain"
    )

@app.get("/stream-chat")
async def stream_chat_endpoint(query: str):


    return StreamingResponse(

        stream_chat(query),

        media_type="text/plain"
    )

@app.post("/chat")
async def chat_endpoint(request: QueryRequest):


    response = chat(

        request.user_id,

        request.query
    )


    return {
        "response": response
    }