__author__ = 'ningyuanyuan1'


class LeiFeng:
    def sweep(self):
        print "LeiFeng sweep"


class Student(LeiFeng):
    def sweep(self):
        print "Student sweep"


class Volenter(LeiFeng):
    def sweep(self):
        print "Volenter sweep"


class LeiFengFactory:
    def createleifeng(self):
        temp = LeiFeng()
        return temp


class StudentFactory(LeiFengFactory):
    def createleifeng(self):
        temp = Student()
        return temp


class VolenterFactory(LeiFengFactory):
    def createleifeng(self):
        temp = Volenter()
        return temp


if __name__ == "__main__":
    sf = StudentFactory()
    s = sf.createleifeng()
    s.sweep()
    sdf = VolenterFactory()
    sd = sdf.createleifeng()
    sd.sweep()