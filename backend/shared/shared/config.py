from slowapi import Limiter
from slowapi.util import get_remote_address
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
KEYS_DIR = BASE_DIR / "secrets"
PRIVATE_KEY_PATH = KEYS_DIR / "private_key.pem"
PUBLIC_KEY_PATH = KEYS_DIR / "public_key.pem"
ENV_DIR = BASE_DIR / "shared" / "shared" / ".env"

def load_key(path: Path) -> bytes:
    with open(path, "rb") as f:
        return f.read()

limiter = Limiter(key_func=get_remote_address)

RSA_PRIVATE_KEY = load_key(PRIVATE_KEY_PATH)
RSA_PUBLIC_KEY = load_key(PUBLIC_KEY_PATH)

load_dotenv(dotenv_path=ENV_DIR)


# SERVICES VARIABLES
AUTH_V1_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://localhost:8001")
USER_V1_SERVICE_URL = os.getenv("USERS_SERVICE_URL", "http://localhost:8002")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# DATABASE VARIABLES
AUTH_DATABASE_URL = os.getenv("AUTH_DATABASE_URL", "http://localhost:8001")
USERS_DATABASE_URL = os.getenv("USERS_DATABASE_URL", "http://localhost:8001")

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_FROM = os.getenv("EMAIL_FROM")

DEBUG_MODE = os.getenv("DEBUG", True)
