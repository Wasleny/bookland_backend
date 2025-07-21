from dotenv import load_dotenv
from pathlib import Path
import os

env_path = env_path = Path(".env").resolve()
load_dotenv(dotenv_path=env_path)


ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@bookland.com")
ADMIN_NAME = os.getenv("ADMIN_NAME", "Super Admin")
ADMIN_NICKNAME = os.getenv("ADMIN_NICKNAME", "super_admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin@Pass123")
ADMIN_AVATAR_URL = os.getenv("ADMIN_AVATAR_URL", "/images/avatars/generic-avatar.svg")

SECRET_KEY = str(os.getenv("SECRET_KEY", ""))
ALGORITHM = str(os.getenv("ALGORITHM", ""))
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

ORIGINS = os.getenv("ORIGINS", "http://localhost:5173,http://0.0.0.0:5173,bookland-wmp.vercel.app").split(
    ","
)

DOCKER_ENV = os.getenv("DOCKER_ENV", "0") == "1"

MONGO_USER = os.getenv("MONGO_USER", "mongouser")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "mongopass")
MONGO_DB = os.getenv("MONGO_DB", "bookland")
MONGO_HOST = "mongo" if DOCKER_ENV else "localhost"
MONGO_PORT = os.getenv("MONGO_PORT", "27017")

MONGO_AUTH_DB = "admin"

if os.getenv("MONGO_URI"):
    MONGO_URI = os.getenv("MONGO_URI")
else:
    MONGO_URI = (
        f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
        f"?authSource={MONGO_AUTH_DB}"
    )
