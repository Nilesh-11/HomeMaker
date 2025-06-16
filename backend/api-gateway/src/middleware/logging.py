import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from src.config.config import logger
from fastapi.responses import JSONResponse
from fastapi import status

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        try:
            response = await call_next(request)
        except Exception as e:
            logger.exception("Unhandled exception occurred during request")
            response = JSONResponse(
                content={"detail": "Internal Server Error"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        process_time = time.time() - start_time
        user_agent = request.headers.get("user-agent", "unknown")
        client_ip = request.client.host
        
        logger.info(
            f"{request.method} {request.url.path} from {client_ip} [{user_agent}] "
            f"-> {response.status_code} in {process_time:.2f}s"
            )

        return response
