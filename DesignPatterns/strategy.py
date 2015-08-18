# coding=utf-8
__author__ = 'ningyuanyuan1'


class CashSuper:
    def accept_cash(self, money):
        return 0


#正常结算
class CashNormal(CashSuper):
    def accept_cash(self, money):
        return money


#打折
class CashRebate(CashSuper):
    discount = 0

    def __init__(self, ds):
        self.discount = ds

    def accept_cash(self, money):
        return money * self.discount


#满减
class CashReturn(CashSuper):
    limit = 0
    ret = 0

    def __init__(self, limit, ret):
        self.limit = limit
        self.ret = ret

    def accept_cash(self, money):
        if money >= self.limit:
            return money - self.ret
        else:
            return money


class CashContext:
    def __init__(self, operation):
        self.cs = operation

    def getresult(self, money):
        return self.cs.accept_cash(money)


if __name__ == '__main__':
    money = input("money:")

    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.6))
    strategy[3] = CashContext(CashReturn(500, 200))

    in_type = input("type:[1]for normal;[2]for 60% discount;[3]for 500-200.")
    if in_type in strategy:
        cc = strategy[in_type]
    else:
        print "Undefine type.User normal mode."
        cc = strategy[1]
    print "You will pay:%d" % (cc.getresult(money))
