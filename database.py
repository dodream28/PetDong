from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("mongodb://petadmin:vptehd12#$56@4.217.178.224:27017/")
client = MongoClient(MONGO_URI)
db = client["pet_health"]


collection = db["health_records"]

# 데이터 삽입
sample_data = {
    "pet_id": "pet001",
    "heart_rate": 95,
    "distance": 3.2,
    "timestamp": "2025-07-11T10:30:00"
}
insert_result = collection.insert_one(sample_data)
print("Inserted ID:", insert_result.inserted_id)

# 데이터 조회
for record in collection.find():
    print(record)

# 데이터 수정
collection.update_one(
    {"pet_id": "pet001"},
    {"$set": {"heart_rate": 100}}
)

# 데이터 삭제
collection.delete_one({"pet_id": "pet001"})