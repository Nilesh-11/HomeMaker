from pydantic import BaseModel, ConfigDict

class AuthRequest(BaseModel):
    model_config = ConfigDict(extra="allow")