import chainlit as cl
import requests

FASTAPI_URL = "http://localhost:8000/chat"

@cl.on_message
async def on_message(message: cl.Message):
    res = requests.post(FASTAPI_URL, json={"message": message.content})
    bot_reply = res.json().get("response", "Something went wrong.")
    await cl.Message(content=bot_reply).send()
