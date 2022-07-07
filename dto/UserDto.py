from pydantic import BaseModel
from fastapi import Body


# 用户注册时需要传递的参数
class RegisterDTO(BaseModel):
    # 用户昵称:必传
    name: str

    # 用户邮箱:必传
    email: str = Body(None, min_length=1, max_length=30,
                      regex=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    # 用户密码:必传
    password: str

    # 用户年龄:可选
    age: int = None

    # 用户手机号:可选
    phone: str = None

    # 用户签名:可选
    desc: str = Body(None, min_length=1, max_length=30)
