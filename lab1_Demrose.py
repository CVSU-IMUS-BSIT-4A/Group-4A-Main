from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Pydantic models
class ItemIn(BaseModel):
    Name: str
    Price: float
    Description: str

class ItemUpdate(BaseModel):
    Name: Optional[str] = None
    Price: Optional[float] = None
    Description: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

items = {
    "1": {"id": 1, "name": "Intel i5 11th Gen", "price": 1000, "description": "Intel i5 11th Gen is a processor that is used in laptops and desktops"},
    "2": {"id": 2, "name": "AMD Ryzen 5 5600G", "price": 1000, "description": "AMD Ryzen 5 5600G is a processor that is used in laptops and desktops"},
    "3": {"id": 3, "name": "AMD Ryzen 7 5800G", "price": 1000, "description": "AMD Ryzen 7 5800G is a processor that is used in laptops and desktops"}
}

@app.get("/items")
def list_items():
    return {"count": len(items), "items": items}

@app.get("/items/{item_id}")
def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items/", status_code=201)
def create_item(item: ItemIn):
    for existing in items.values():
        if existing.get("name", "").lower() == item.Name.lower():
            raise HTTPException(status_code=400, detail="Item already Exist")
    new_id = str(max(int(k) for k in items.keys()) + 1) if items else "1"
    items[new_id] = {"id": int(new_id), "name": item.Name, "price": item.Price, "description": item.Description}
    return {"id": int(new_id), **items[new_id]}

@app.put("/items/{item_id}")
def update_item(item_id: str, update: ItemUpdate = Body(..., example={"Name": "Updated Name", "Price": 123.45, "Description": "Updated description"})):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    if update.Name:
        for eid, existing in items.items():
            if eid != item_id and existing.get("name", "").lower() == update.Name.lower():
                raise HTTPException(status_code=400, detail="Item already Exist")
        items[item_id]["name"] = update.Name
    if update.Price is not None:
        items[item_id]["price"] = update.Price
    if update.Description is not None:
        items[item_id]["description"] = update.Description
    return {"id": int(item_id), **items[item_id]}