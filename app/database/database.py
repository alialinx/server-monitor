from pymongo import MongoClient
from app.settings.config import MONGO_URI, MONGO_DB_NAME

client = MongoClient(MONGO_URI)

from fastapi import FastAPI, Depends
app = FastAPI()

def get_db():
    return client[MONGO_DB_NAME]


@app.on_event("shutdown")
def shutdown_db_client():
    client.close()