from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from main import generate_report

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    company: str
    problem: str

@app.get("/")
def home():
    return {
        "message": "GreenLoom AI Consultant API Running"
    }

@app.post("/analyze")
def analyze(data: AnalysisRequest):

    report = generate_report(
        data.company,
        data.problem
    )

    return {
        "report": report
    }