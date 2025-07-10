from fastapi import FastAPI
from database import db
from models import HealthRecord
from bson import ObjectId

app = FastAPI()

collection = db["health_records"]  # 컬렉션 지정

@app.post("/records")
def create_record(record: HealthRecord):
    result = collection.insert_one(record.dict())
    return {"inserted_id": str(result.inserted_id)}

@app.get("/records")
def read_records():
    records = []
    for record in collection.find():
        record["_id"] = str(record["_id"])  # ObjectId 문자열 변환
        records.append(record)
    return records
