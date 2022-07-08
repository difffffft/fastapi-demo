import os
import uuid
from typing import Union
from fastapi import APIRouter, UploadFile
from common.R import R
from common.Context import SOCKET_USERS
from model.User import User

from dto.UserDto import RegisterDTO

router = APIRouter()


# 分页查询
@router.post("/page")
async def get_users_by_page(skip: int = None, limit: int = 10):
    return R.success("成功", limit)


# 用户登录
@router.post("/login")
async def login(item):
    return "login"


# 用户注册
@router.post("/register")
async def register(reg: RegisterDTO):
    user = User(**vars(reg))
    user.create_table(True)
    b = user.insert()
    if b:
        return R.success("注册成功", reg)
    else:
        return R.error("注册失败")


@router.post("/upload/images")
async def upload_images(file: Union[UploadFile, None] = None):
    if not file:
        return R.error("未选择文件")
    file_name_list = file.filename.split('.')
    file_name = str(uuid.uuid4()) + "." + file_name_list[-1]
    file_path = f'./static/images/'
    os.makedirs(file_path, mode=0o777, exist_ok=True)
    file_path += file_name
    file_bytes = await file.read()
    with open(file_path, "wb+") as f:
        f.write(file_bytes)
    return R.success("上传成功", file_path)
