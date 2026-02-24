from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class AnalyzeRequest(BaseModel):
    text: str

@app.get("/")
def health():
    return {"durum": "hazır", "servis": "norya-api"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Bu kan tahlili ifadesini hastaya anlaşılır şekilde açıkla: {req.text}"
    )
    return {
        "sonuc": response.output_text,
        "not": "Norya AI yorumladı."
    }   