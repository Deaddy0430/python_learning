# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score=score

# s1 = Student('xzx', 52)
# print(s1.score)
# s1.socre=100    #the score spelling wrong, but it won't show error
# print(s1.score)

class Student:
    __slots__=['name', 'score'] #so this class only has these 2 element.
    def __init__(self, name, score):
        self.name = name
        self.score=score

s1 = Student('xzx', 52)
print(s1.score)
#s1.socre=100    #it will show error now
s1.score=100
print(s1.score)