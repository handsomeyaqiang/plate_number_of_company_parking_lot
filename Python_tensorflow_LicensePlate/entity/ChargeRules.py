class ChargeRules:
    '收费规则'
    def __init__(self,rid,dayprice,nightprice,daybegintime,dayendtime,
                 nightbegintime,nightendtime,firsthourprice):
        self.rid = rid
        self.dayprice = dayprice
        self.nightprice = nightprice
        self.daybegintime = daybegintime
        self.dayendtime = dayendtime
        self.nightbegintime = nightbegintime
        self.nightendtime = nightendtime
        self.firsthourprice = firsthourprice
