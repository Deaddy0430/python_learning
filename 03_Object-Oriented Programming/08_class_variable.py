#this is an application for class variable

class  Car:
    count = 0
    def __init__(self, info):
        print(info, "is created")
        self.data = info
        self.__class__.count += 1
    def __del__(self):
        print(self.data, "is deleted")
        self.__class__.count -= 1

print('The current total amount of car is', Car.count)
b1=Car("BYD: DVF.98H")
print(Car.count)
b2=Car("Tesla: DMG92T")
b3=Car("Tiguan: DDD999")
print('The current total amount of car is', Car.count)
del b1
del b2
print('The current total amount of car is', Car.count)