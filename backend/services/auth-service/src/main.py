from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from src.routes.google import router as google_router
from src.middleware.logging import LoggingMiddleware
from starlette.middleware.sessions import SessionMiddleware
from src.config.config import SECRET_KEY
from shared.db_models.base import BaseAuth, engine_auth
app = FastAPI(title="Auth Service")

BaseAuth.metadata.create_all(bind=engine_auth)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

app.include_router(google_router, prefix="/google")

origins = [
    "http://localhost:8000",
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
