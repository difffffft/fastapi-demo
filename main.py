import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles

from router import UserRouter
from handler import request_validation_exception_handler, exception_handler
from middleware import TokenMiddleware
from middleware import SignMiddleware

# 全局app
app = FastAPI()
# 静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")
# 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
# token校验
app.add_middleware(TokenMiddleware)
# 接口加密校验
app.add_middleware(SignMiddleware)
# 接口参数格式校验异常全局捕获
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
# 异常全局捕获
app.add_exception_handler(Exception, exception_handler)
# 全局接口前缀
global_prefix = "/api"
# 注册用户路由
app.include_router(UserRouter.router, prefix=global_prefix + "/user")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


# 运行入口
if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
