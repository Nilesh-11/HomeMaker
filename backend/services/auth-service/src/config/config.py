import os
import logging
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth
import datetime

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("api_gateway")
logger.setLevel(logging.DEBUG)

info_handler = logging.FileHandler("logs/auth-service.log")
info_handler.setLevel(logging.INFO)
info_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
info_handler.setFormatter(info_formatter)

error_handler = logging.FileHandler("logs/auth-service-errors.log")
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
error_handler.setFormatter(error_formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)

GOOGLE_CLIENT_ID=os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET=os.getenv("GOOGLE_CLIENT_SECRET")
SECRET_KEY=os.getenv("SECRET_KEY"),

config_data = {
    "GOOGLE_CLIENT_ID": GOOGLE_CLIENT_ID,
    "GOOGLE_CLIENT_SECRET": GOOGLE_CLIENT_SECRET,
    "SECRET_KEY": SECRET_KEY,
}

config = Config(environ=config_data)

oauth = OAuth(config)
oauth.register(
    name="google",
    client_id=config_data["GOOGLE_CLIENT_ID"],
    client_secret=config_data["GOOGLE_CLIENT_SECRET"],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

JWT_TOKEN_EXPIRY=datetime.timedelta(minutes=int(os.getenv("JWT_TOKEN_EXPIRY", 15))) # seconds
REFRESH_TOKEN_EXPIRY=datetime.timedelta(minutes=int(os.getenv("REFRESH_TOKEN_EXPIRY", 360))) # seconds