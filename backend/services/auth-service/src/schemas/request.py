from pydantic import BaseModel

class googleLoginRequest(BaseModel):
    token: str