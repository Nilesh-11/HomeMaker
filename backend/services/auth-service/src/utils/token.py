import time
import jwt
from shared.config import RSA_PRIVATE_KEY, RSA_PUBLIC_KEY
from src.config.config import JWT_TOKEN_EXPIRY
from typing import List

def get_jwt_token(id: str, role: str, aud: str, scp: str):
    curr_time = int(time.time())
    payload = {
        "iss": "HomeMaker",
        "sub": str(id),
        "aud": aud,
        "role": role,
        "exp": curr_time + int(JWT_TOKEN_EXPIRY.total_seconds()),
        "nbf": curr_time,
        "iat": curr_time,
        "jti": "auth",
        "scp": scp,
    }
    token = jwt.encode(payload, RSA_PRIVATE_KEY, algorithm="RS256")
    return token

def verify_jwt(token, aud):
    data = jwt.decode(token, RSA_PUBLIC_KEY, algorithms=["RS256"], audience=aud)
    return data