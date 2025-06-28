from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

DOCKER_ENV = os.getenv("DOCKER_ENV", "0") == "1"

MONGO_USER = os.getenv("MONGO_USER", "mongouser")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "mongopass")
MONGO_DB = os.getenv("MONGO_DB", "bookland")
MONGO_HOST = "mongo" if DOCKER_ENV else "localhost"
MONGO_PORT = os.getenv("MONGO_PORT", "27017")

MONGO_AUTH_DB = "admin"

MONGO_URI = (
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    f"?authSource={MONGO_AUTH_DB}"
)
