from fastapi import APIRouter, Request
from src.services.user_service import forward_user_request

router = APIRouter()

@router.api_route("/{path:path}", methods=["POST", "GET", "PUT", "DELETE", "OPTIONS", "PATCH"])
async def auth_request(path: str, request: Request):
    full_path = request.url.path
    client_ip = request.client.host
    existing_xff = request.headers.get("x-forwarded-for")
    if existing_xff:
        x_forwarded_for = f"{existing_xff}, {client_ip}"
    else:
        x_forwarded_for = client_ip
    custom_headers = {
        "x-forwarded-for": x_forwarded_for,
    }
    return await forward_user_request(request, full_path, custom_headers)
