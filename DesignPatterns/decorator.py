__author__ = 'ningyuanyuan1'


class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print "dressed %s" % self.name


class Finery(Person):
    component = None

    def __init__(self):
        pass

    def decorator(self, ct):
        self.component = ct

    def show(self):
        if self.component is not None:
            self.component.show()


class TShirts(Finery):
    def __init__(self):
        pass

    def show(self):
        print "Big T-shirt"
        self.component.show()


class BigTrouser(Finery):
    def __init__(self):
        pass

    def show(self):
        print "BigTrouser"
        self.component.show()


if __name__ == "__main__":
    p = Person("Lucy")
    bt = BigTrouser()
    ts = TShirts()

    ts.decorator(p)
    bt.decorator(ts)
    bt.show()