from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class articulos(BaseModel)
    name: str
    price: float
    is_offer: Union [bool,None] = None
    

@app.get("/obten/items/{item_id}")
def getitem()

