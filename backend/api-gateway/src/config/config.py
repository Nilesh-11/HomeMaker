import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("api_gateway")
logger.setLevel(logging.DEBUG)

info_handler = logging.FileHandler("logs/api-gateway.log")
info_handler.setLevel(logging.INFO)
info_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
info_handler.setFormatter(info_formatter)

error_handler = logging.FileHandler("logs/api-gateway-errors.log")
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
error_handler.setFormatter(error_formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)
