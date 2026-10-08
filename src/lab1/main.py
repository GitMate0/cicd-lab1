from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()

db = {
    "Test": {"id": "Test", "title": "Title", "description": "Description"}
}

class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


@app.get("/items/")
def read_items():
    return db

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

@app.post("/items/")
def create_item(item: Item):
    if item.id in db:
        raise HTTPException(status_code=409, detail="Item already exists")
    db[item.id] = item
    return item

@app.put("/items/{item_id}")
def update_item(item_id: str, item_data: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = Item(
        id=item_id,
        title=item_data.title,
        description=item_data.description
    )
    db[item_id] = updated_item.model_dump()
    return db[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db.pop(item_id)
    return None
