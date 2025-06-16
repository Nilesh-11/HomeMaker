from fastapi import APIRouter, Request
from src.services.auth_service import forward_auth_request

router = APIRouter()

@router.api_route("{path:path}", methods=["POST", "GET", "PUT", "DELETE", "OPTIONS", "PATCH"])
async def auth_request(path: str, request: Request):
    query_string = str(request.query_params)
    full_path = f"{path}?{query_string}" if query_string else path
    client_ip = request.client.host
    existing_xff = request.headers.get("x-forwarded-for")
    if existing_xff:
        x_forwarded_for = f"{existing_xff}, {client_ip}"
    else:
        x_forwarded_for = client_ip
    custom_headers = {
        "x-forwarded-for": x_forwarded_for,
    }
    return await forward_auth_request(request, full_path, custom_headers)
