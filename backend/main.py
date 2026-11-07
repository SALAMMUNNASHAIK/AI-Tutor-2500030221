from fastapi import FastAPI

klu = FastAPI(title="AI TUTOR", 
              description="AI Tutor pbl Project",
              version="1.0.0")

@klu.get("/")
def home():
    return {"message":"Welcome to AI Tutor Project"}

@klu.get("/demo")
def demo():
    return{"message":"KL UNIVERSITY"}

@klu.get("/askquestion")
def ask():
    return{"message":"What is llm","answer":"large language model"}