from fastapi import FastAPI
from pydantic import BaseModel

from app.models.Item import Item

app = FastAPI(title="FAST API STARTER", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Hello basic app"}

@app.get("/profile/{profile_id}")
def get_profile(profile_id: int):
    return {"profile_id": profile_id}

@app.post("/items")
def post_item(item: Item):
    return {"status": "Item added successfully"}