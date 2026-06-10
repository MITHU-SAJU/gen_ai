from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(data: Question):

    response = client.responses.create(
        model="gpt-5-mini",
        input=data.question
    )

    return {
        "answer": response.output_text
    }

@app.get("/tell")
def tell_answer():
    response = client.responses.create(
        model="gpt-5-mini",
        input="Tell me a joke."
    )

    return {
        "answer": response.output_text
    }