__author__ = 'ningyuanyuan1'

import copy


class WorkExp:
    place = ""
    year = ()


class Resume:
    name = ''
    age = 0
    work_exp = WorkExp()

    def __init__(self, n):
        self.name = n

    def set_age(self, a):
        self.age = a

    def set_workexp(self, p, y):
        self.work_exp.place = p
        self.work_exp.year = y

    def display(self):
        print self.name, self.age, self.work_exp.place, self.work_exp.year

    def clone(self):
        new_obj = copy.copy(self)
        new_obj.work_exp = copy.copy(self.work_exp)
        return new_obj


if __name__ == "__main__":
    a = Resume('Lucy')
    a.set_workexp('bawei', 5)
    a.set_age(22)

    b = a.clone()
    b.set_workexp('bawei', 6)
    b.set_age(23)

    a.display()
    b.display()