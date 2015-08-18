__author__ = 'ningyuanyuan1'


class TestPaper:
    def test_question1(self):
        print "Test1:A. B. C. D."
        print '%s' % self.answer1()

    def test_question2(self):
        print "Test2:A. B. C. D."
        print '%s' % self.answer2()

    def answer1(self):
        return ""

    def answer2(self):
        return ""


class TestPaperA(TestPaper):
    def answer1(self):
        return "A"

    def answer2(self):
        return "B"


class TestPaperB(TestPaper):
    def answer1(self):
        return "C"

    def answer2(self):
        return "D"


if __name__ == "__main__":
    s1 = TestPaperA()
    s2 = TestPaperB()
    print "Student 1:"
    s1.test_question1()
    s1.test_question2()
    print "Student 2:"
    s2.test_question1()
    s2.test_question2()