from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Hello World"}


#Path Parameters (параметри шляху)
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


#Query Parameters (параметри запиту)
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}