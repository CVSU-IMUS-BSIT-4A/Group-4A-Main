from fastapi import FastAPI, HTTPException
app = FastAPI()


items = {
    1: {"Name": "Intel i5 11th Gen",
    "Price": "10000",
    "Description": "Intel i5 11th Gen is a processor that is used in laptops and desktops.",
    },
    2: {"Name": "AMD Ryzen 5 5600G",
    "Price": "10000",
    "Description": "AMD Ryzen 5 5600G is a processor that is used in laptops and desktops.",
    },
    3: {"Name": "AMD Ryzen 7 5800H",
    "Price": "10000",
    "Description": "AMD Ryzen 7 5800H is a processor that is used in laptops and desktops.",
    },
}

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]