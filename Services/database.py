from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = "evho_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]