from fastapi import Request
from fastapi.responses import JSONResponse, Response
import httpx
from shared.config import AUTH_V1_SERVICE_URL
from src.config.config import logger

UNSAFE_HEADERS = {"host", "content-length", "connection"}

async def forward_auth_request(request: Request, full_path: str, injected_headers: dict) -> Response:
    method = request.method
    url = f"{AUTH_V1_SERVICE_URL}{full_path}"

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

        forwarded_response = Response(
            content=response.content,
            status_code=response.status_code,
            media_type=response.headers.get("content-type", "application/json")
        )
        
        for key, value in response.headers.multi_items():
            if key.lower() not in UNSAFE_HEADERS and key.lower() != "set-cookie":
                forwarded_response.headers.append(key, value)

        return forwarded_response
    except Exception as e:
        logger.error("Error in forwarding auth request: ", e)
        return JSONResponse(
            status_code=503,
            content={"error": "Gateway Error", "details": str(e)}
        )
