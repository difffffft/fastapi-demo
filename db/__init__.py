from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456@192.168.2.80:3306/demo?charset=utf8', echo=True)
DBSession = sessionmaker(bind=engine)


class BaseModel(declarative_base()):
    __abstract__ = True

    # 建表
    # is_del:是否删除重建
    def create_table(self, is_del: bool = False):
        if is_del:
            self.drop_table()
        self.metadata.create_all(engine)

    # 删表
    def drop_table(self):
        self.metadata.drop_all(engine)

    # 新增数据
    def insert(self):
        res = True
        session = DBSession()
        session.add(self)
        try:
            session.commit()
        except Exception as e:
            print(e)
            res = False
        finally:
            session.close()
        return res

    # 删除数据
    def delete(self):
        pass

    # 更新数据
    def update(self):
        pass

    # 查找数据
    def find_all(self):
        pass

    # 根据ID找数据
    def find_by_id(self):
        pass
