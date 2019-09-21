#default inherit from "object" class
class Human:    #this line can be written as "class Human(object)"
    def say(self, that):
        print("say:", that)
    def walk(self, distance):
        print("walk %d steps" % distance)

class Student(Human):
    def study(self, subject):
        print("is learning", subject)

class Teacher(Student):
    def teach(self, subject):
        print("is teaching", subject)

h1 = Human()
h1.say("Todat is so hot")
h1.walk(4000)

print('---------below are the student/teacher objects--------')
s1 = Student()
s1.say("I hate study")
s1.walk(10000)
s1.study("Python")

t1 = Teacher()
t1.say("tmr is weekend")
t1.walk(200)
t1.teach("python oop")
t1.study("English")

print("Human belongs to ", Human.__base__)
print("Student belongs to ", Student.__base__)
print("Teacher belongs to ", Teacher.__base__)