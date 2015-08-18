__author__ = 'ningyuanyuan1'
#coding=utf-8


class Operation:
    def getresult(self):
        pass


class OperationAdd(Operation):
    def getresult(self):
        return self.op1 + self.op2


class OperationSub(Operation):
    def getresult(self):
        return self.op1 - self.op2


class OperationMul(Operation):
    def getresult(self):
        return self.op1 * self.op2


class OperationDiv(Operation):
    def getresult(self):
        try:
            result = self.op1 / self.op2
            return result
        except:
            print "error:divided by zero"
            return 0


class OperationUndef(Operation):
    def getresult(self):
        print "Undefine operation."
        return 0


class OperationFactory:
    operation = {}
    operation["+"] = OperationAdd();
    operation["-"] = OperationSub();
    operation["*"] = OperationMul();
    operation["/"] = OperationDiv();

    def create_operate(self, ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op


if __name__ == "__main__":
    op = raw_input("operation:")
    opa = input("a:")
    opb = input("b:")
    factory = OperationFactory()
    cal = factory.create_operate(op)
    cal.op1 = opa
    cal.op2 = opb
    print cal.getresult()
