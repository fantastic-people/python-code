class Person(object):
    sum  = 0
    def wwork(self):
        print('waaa')
    # def __init__(self, name, gender):
    #     self.name = name
    #     self.gender = gender


class Student(Person):
    def work(self):
        print('aaa')

    # def __init__(self, name, gender, score):
        # super(Student, self).__init__(name, gender)
        # self.score = score
    
s = Student()
s.sum=1
print(s.sum)
s.work()
s.wwork()