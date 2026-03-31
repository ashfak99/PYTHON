from fastapi import FastAPI
from mockData import mockdata

app=FastAPI()

@app.get("/")
async def hello():
    return "Hi From Server"

@app.get("/item")
async def items():
    return mockdata
