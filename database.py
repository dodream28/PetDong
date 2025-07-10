import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["pet_health"]  # DB 이름
