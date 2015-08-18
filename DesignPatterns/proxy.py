__author__ = 'ningyuanyuan1'


class Interface():
    def __init__(self):
        pass

    def request(self):
        return 0


class RealSubject(Interface):
    def __init__(self):
        pass

    def request(self):
        print "Real Request."


class Proxy(Interface):
    def __init__(self):
        pass

    def request(self):
        self.real = RealSubject()
        self.real.request()


if __name__ == "__main__":
    p = Proxy()
    p.request()