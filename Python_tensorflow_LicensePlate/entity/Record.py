class Record:
    ''' 停车进出记录类
        rid 记录的id自增字段
        platenumber 车辆的车牌号
        intime 车辆进入的时间
        outtime 车辆离开的时间
        vehicletype 进入的车辆类型：外部车或者内部车
        feestatus 外部的车辆是否缴费
    '''

    def __init__(self, rid, platenumber, intime, outtime, vehicletype, feestatus):
        self.rid = rid
        self.platenumber = platenumber
        self.intime = intime
        self.outtime = outtime
        self.vehicletype = vehicletype
        self.feestatus = feestatus