class Student:
    def set_info(self, name, age=0):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, '今年', self.age, '岁')

s1 = Student()
s1.set_info('小张',20)

s2 = Student()
s2.set_info('小李', 18)

s1.show_info()
s2.show_info()