#modified from 03_example.py
class Student:
    def __init__(self, name, age=0, score=0):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print(self.name, '今年', self.age, '岁', '成绩是', self.score)

    def set_score(self, sc):
        self.score = sc

s1 = Student('小张', 20)

s2 = Student('小李', 18, 100)

s1.set_score(90)

s1.show_info()
s2.show_info()