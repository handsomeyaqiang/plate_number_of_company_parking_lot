# 停车场自定义返回结构 status：返回的状态码，正常：200
# msg: 返回的消息
# data：返回的数据


class ParkResult:
    def __init__(self):
        self.status = 200
        self.msg = "OK"
        self.data = None


    # 有数据的正常返回
    def ok(self, data):
        result = ParkResult()
        result.__setattr__("data", data)
        return result

    # 无数据的正常返回
    def ok2(self):
        result = ParkResult()
        return result

    # 带错误消息的异常返回
    def error(self, msg):
        result = ParkResult()
        result.__setattr__("msg", msg)
        result.__setattr__("status", 400)
        return result
