class A:
    def work(self):
        print("A.work() is called")

class B(A):
    def work(self): #define another same function as in A
        print("B.work() is called")    #this will be overwrite
    def super_work(self):
        super().work()

b=B()
b.work()

c=B()
super(B, c).work()  #调用父类work()方法

d=B()
d.super_work()

a=A()
a.work()