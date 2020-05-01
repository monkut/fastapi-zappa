from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.wsgi import WSGIMiddleware


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.post("/items/")
def create_item(item: Item):
    return item


app = WSGIMiddleware(app)
