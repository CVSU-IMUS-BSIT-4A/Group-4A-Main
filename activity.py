from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {1: "Oppo", 2: "Vivo", 3: "Samsung"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}