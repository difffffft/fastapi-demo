import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from router import UserRouter
from common.R import R
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

# 全局app
app = FastAPI()

# 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# 2.请求之前校验token
@app.middleware("http")
async def check_token(request: Request, call_next):
    response = await call_next(request)
    return response


# 1.请求之前校验sign
@app.middleware("http")
async def check_sign(request: Request, call_next):
    response = await call_next(request)
    return response


# 格式校验异常捕获
@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(request: Request, e: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=R.error(str(e.errors())),
    )


# 全局异常捕获
@app.exception_handler(Exception)
async def exception_handler(request: Request, e: Exception):
    print(e)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=R.error(str(e)),
    )


# 全局接口前缀
global_prefix = "/api"

# 注册路由模块
app.include_router(UserRouter.router, prefix=global_prefix + "/user")

# 运行入口
if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
