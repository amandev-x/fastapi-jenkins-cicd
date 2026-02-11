from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel 
import json
app = FastAPI(
    title="FastAPI-Project-with-Jenkins",
    description="Building a simple fastapi project to practice jenkins",
    version="1.0.0" 
)

class Item(BaseModel):
    name: str 
    price: float 

items_db = []

@app.get("/")
async def root():
    return {"message": "Welcome to Jenkins FastAPI Learning Project-1", "status": "healthy"}

@app.get("/items")
async def get_items():
    return {"items": items_db}

@app.post("/items", status_code=201)
async def create_items(item: Item):
    items_db.append(item.dict())
    return {"message": "Item created successfully"}

@app.get("/health")
async def health():
    return {"status": "ok"}



