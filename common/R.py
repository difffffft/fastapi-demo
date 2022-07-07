# 统一前端返回值
class R:

    @staticmethod
    def success(message: str, data):
        return {
            "success": True,
            "message": message,
            "data": data
        }

    @staticmethod
    def error(message: str):
        return {
            "success": False,
            "message": message,
            "data": None
        }
