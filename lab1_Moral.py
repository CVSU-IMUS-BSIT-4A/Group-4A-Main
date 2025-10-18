from fastapi import FastAPI, HTTPException, Body, Response
from pydantic import BaseModel, Field
from typing import Optional, Dict


app = FastAPI()


class ItemIn(BaseModel):
    Name: str = Field(..., min_length=1)
    Price: float = Field(..., ge=0)
    Description: Optional[str] = None


class ItemUpdate(BaseModel):
    Name: Optional[str] = Field(None, min_length=1)
    Price: Optional[float] = Field(None, ge=0)
    Description: Optional[str] = None


# In-memory store
items: Dict[int, Dict] = {
    1: {"Name": "Intel Core i5-11400F", "Price": 9500.0, "Description": "6-core 11th Gen Intel processor ideal for mid-range gaming and productivity."},
    2: {"Name": "AMD Ryzen 5 5600G", "Price": 9800.0, "Description": "6-core CPU with integrated Radeon graphics, great for budget gaming PCs."},
    3: {"Name": "AMD Ryzen 7 5800X", "Price": 16500.0, "Description": "8-core high-performance CPU for gaming and heavy multitasking workloads."},
    4: {"Name": "Intel Core i7-12700K", "Price": 21000.0, "Description": "12th Gen Intel processor with hybrid architecture for top-tier performance."},
    5: {"Name": "NVIDIA GeForce RTX 3060", "Price": 23000.0, "Description": "Mid-range graphics card capable of ray tracing and smooth 1080p/1440p gaming."},
    6: {"Name": "Corsair Vengeance LPX 16GB DDR4", "Price": 4500.0, "Description": "High-speed memory kit for gaming PCs and workstation builds."},
}


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/items")
def list_items():
    return {"count": len(items), "items": items}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items/", status_code=201)
def create_item(item: ItemIn):
    for existing in items.values():
        if existing.get("Name", "").lower() == item.Name.lower():
            raise HTTPException(status_code=400, detail="Item already Exist")
    new_id = max(items.keys()) + 1 if items else 1
    items[new_id] = {"Name": item.Name, "Price": item.Price, "Description": item.Description}
    return {"id": new_id, **items[new_id]}


@app.put("/items/{item_id}")
def update_item(item_id: int, update: ItemUpdate = Body(..., example={"Name": "Updated Name", "Price": 123.45, "Description": "Updated description"})):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    if update.Name:
        for eid, existing in items.items():
            if eid != item_id and existing.get("Name", "").lower() == update.Name.lower():
                raise HTTPException(status_code=400, detail="Item already Exist")
        items[item_id]["Name"] = update.Name
    if update.Price is not None:
        items[item_id]["Price"] = update.Price
    if update.Description is not None:
        items[item_id]["Description"] = update.Description
    return {"id": item_id, **items[item_id]}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return Response(status_code=204)


