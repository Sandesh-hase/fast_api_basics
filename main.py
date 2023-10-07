from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"


food_items = {
    "indian": ["Samosa", "Dosa"],
    "american": ["Alaska", "Pie"],
    "italian": ["Ravioli", "Pizza"],
}

valid_cuisines = food_items.keys()


@app.get("/hello/{name}")
async def hello(name):
    return f"Welcome to the fast api {name}"


@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    if cuisine not in valid_cuisines:
        return f"Valid cusines are only {valid_cuisines}"
    else:
        return food_items.get(cuisine)


@app.get("/get_foods/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)
