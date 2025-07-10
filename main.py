from fastapi import FastAPI
from database import db

app = FastAPI()

@app.post("/pets")
def register_pet(pet: dict):
    pets_collection = db["pets"]
    result = pets_collection.insert_one(pet)
    return {"inserted_id": str(result.inserted_id)}

@app.get("/pets")
def get_all_pets():
    pets_collection = db["pets"]
    pets = list(pets_collection.find({}, {"_id": 0}))
    return {"pets": pets}
