from sqlalchemy import Column, Integer, String, Boolean
from db import BaseModel


# 基础模型
class User(BaseModel):
    # 表名
    __tablename__ = 'user'

    # 主键自增
    id = Column(Integer, primary_key=True, autoincrement=True)

    # 用户邮箱地址
    email = Column(String(255), unique=True)

    # 用户密码
    password = Column(String(255))

    # 男孩
    boy = Column(Boolean, default=True)
