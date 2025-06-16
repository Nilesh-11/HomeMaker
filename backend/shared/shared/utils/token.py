import jwt
from shared.config import RSA_PUBLIC_KEY

def verify_token(token, audience):
    data = jwt.decode(token, RSA_PUBLIC_KEY, algorithms=["RS256"], audience=audience)
    return data