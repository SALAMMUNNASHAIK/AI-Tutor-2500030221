from fastapi import FastAPI
import uvicorn

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

@klu.get("/student")
def student():
    return{"id":1,"name":"Munna","gender":"Male","course":"DSA"}

@klu.get("/students")
def getstudents():
    return[
        {"id":1,"name":"Munna","gender":"Male","course":"GEN-AI"},
        {"id":2,"name":"Priya","gender":"Female","course":"ML"},
        {"id":3,"name":"Rahul","gender":"Male","course":"AI"}
    ]
if __name__=="__main__":
    uvicorn.run("main:klu",host="127.0.0.1",port=2027,reload=True)
