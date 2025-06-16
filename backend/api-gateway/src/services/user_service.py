from fastapi import Request
from fastapi.responses import JSONResponse, Response
import httpx
from shared.config import USER_V1_SERVICE_URL

UNSAFE_HEADERS = {"host", "cookie", "content-length", "connection"}

async def forward_user_request(request: Request, full_path: str, injected_headers: dict) -> Response:
    method = request.method
    url = f"{USER_V1_SERVICE_URL}{full_path}"

    headers = {
        k: v for k, v in request.headers.items()
        if k.lower() not in UNSAFE_HEADERS
    }

    headers.update(injected_headers)

    body = await request.body() if method in ["POST", "PUT", "PATCH"] else None

    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=method,
                url=url,
                headers=headers,
                content=body
            )
        return Response(
            content=response.content,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.headers.get("Content-Type", "application/json")
        )
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={"error": "Gateway Error", "details": str(e)}
        )
