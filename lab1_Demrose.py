from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

items = {
    "1": {"id": 1, "name": "Intel i5 11th Gen", "price": 1000, "description": "Intel i5 11th Gen is a processor that is used in laptops and desktops"},
    "2": {"id": 2, "name": "AMD Ryzen 5 5600G", "price": 1000, "description": "AMD Ryzen 5 5600G is a processor that is used in laptops and desktops"},
    "3": {"id": 3, "name": "AMD Ryzen 7 5800G", "price": 1000, "description": "AMD Ryzen 7 5800G is a processor that is used in laptops and desktops"}
}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]