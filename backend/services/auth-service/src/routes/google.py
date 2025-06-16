from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
from src.schemas.request import googleLoginRequest
from src.config.config import GOOGLE_CLIENT_ID
from src.utils.token import get_jwt_token
from shared.db_models.user import User
import os
router = APIRouter()

@router.post("/login")
async def google_token(payload: googleLoginRequest, response: Response):
    try:
        idinfo = id_token.verify_oauth2_token(
            payload.token,
            grequests.Request(),
            GOOGLE_CLIENT_ID
        )
        # print(idinfo)
        user = User(
            name=idinfo["name"],
            email = idinfo["email"],
        )
        google_user_id = idinfo["sub"],
        jwt_token = get_jwt_token(id=1, role="user", aud="dev", scp="read write") 
        response = JSONResponse(content={"type": "ok", "userId": 1}, status_code=200)
        response.headers["x-jwt-token"] = jwt_token
        return response

    except Exception as e:
        print("Error in login with google", e)
        raise HTTPException(status_code=400, detail="Invalid Google token")
