class Human():
    def __init__(self,n,a):
        self.name = n
        self.age = a

    def infos(self):
        print("name: ", self.name)
        print("age: ", self.age)

class Student(Human):
    def __init__(self,n,a,s=0):
        super().__init__(n, a)
        self.score = s

    def infos(self):
        super().infos()
        print("score: ", self.score)
    
s1 = Student('David', 18, 32)
s1.infos()