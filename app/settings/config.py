import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

# -----------------------------
# MongoDB Bağlantı Ayarları
# -----------------------------
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_DB_USER = os.getenv("MONGO_DB_USER")
MONGO_DB_PASS = os.getenv("MONGO_DB_PASS")
MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE")

MONGO_URI = (
    f"mongodb://{MONGO_DB_USER}:{MONGO_DB_PASS}"
    f"@{MONGO_HOST}:{MONGO_PORT}/"
    f"?authSource={MONGO_AUTH_SOURCE}"
)


# -----------------------------
# Auth & Token Ayarları
# -----------------------------
TOKEN_URL = "/login"
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
TOKEN_EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRE_MINUTES"))


# -----------------------------
# Swagger Basic Auth
# -----------------------------
SWAGGER_USER = os.getenv("SWAGGER_USER")
SWAGGER_PASS = os.getenv("SWAGGER_PASS")
