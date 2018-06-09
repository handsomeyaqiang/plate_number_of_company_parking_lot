class ParkLock:
    """车位锁类

     attributes:
     parklock_number :车锁编码
     parklock_status :车锁状态 0 开 1 锁
    """
    def __init__(self,ParkLockID,status):
        """Inits ParkLock """
        self.ParkLockID = ParkLockID
        self.status = status




