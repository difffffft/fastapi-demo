from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware


# Token校验中间件
class TokenMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        print("token校验中")
        response = await call_next(request)
        return response


# 接口加密校验中间件
class SignMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        print("sign校验中")
        response = await call_next(request)
        return response
