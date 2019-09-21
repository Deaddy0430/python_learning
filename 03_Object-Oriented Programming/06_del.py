class Car:
    def __init__(self, c, b, m):
        self.color = c
        self.brand = b
        self.model = m
    def __del__(self):
        print(self.model, "对象已经销毁")

a4 = Car('红色', '奥迪', 'A4')
# del a4
a4 = Car('蓝色', 'Tesla', 'Model S')
# a4 will be delete when program terminated
# while True:
#     pass