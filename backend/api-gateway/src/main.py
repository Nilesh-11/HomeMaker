from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from starlette.responses import JSONResponse
from src.routes.v1.auth import router as auth_v1_router
from src.routes.v1.user import router as user_v1_router
from src.middleware.logging import LoggingMiddleware
app = FastAPI(title="API Gateway")

app.include_router(auth_v1_router, prefix="/v1/auth")
app.include_router(user_v1_router, prefix="/v1/user")

origins = [
    "http://localhost:3000",
]

custom_headers = [
    "x-jwt-token",
    "x-refresh-token",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET", "DELETE", "PUT", "UPDATE", "OPTIONS", "PATCH"],
    allow_credentials=True,
    allow_headers=["*"],
    expose_headers=custom_headers,
)
app.add_middleware(LoggingMiddleware)

@app.get("/")
def health_check(request: Request):
    return JSONResponse(
                content= {
                    "status": "Event Service is running"
                }
            )
