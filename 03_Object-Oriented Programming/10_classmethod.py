class Car:
    count = 0

    @classmethod    #the first elecment is cls
    def getTotalCount(cls):
        return cls.count
    @classmethod
    def increment(cls, num):
        cls.count += num

print(Car.getTotalCount())

#Car.count +=1 # OOP不提倡直接操作里面的属性
c1=Car()
c1.increment(10)
print(c1.getTotalCount())