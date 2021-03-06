class Car:
    def __init__(self, c, b, m):
        self.color = c
        self.brand = b
        self.model = m

    def run(self, speed):
        print(self.color, '的', self.brand, self.model, '正在以', speed, 'km/s 的速度行驶着')

    def set_color(self, clr):
        self.color = clr

a4 = Car('红色', '奥迪', 'A4')
# a4.__init__('white', 'Tesla', 'Model S')  显示调用
a4.run(179)
a4.set_color('黑色')
a4.run(300)

t1 = Car('蓝色', 'Tesla', 'Model S')
t1.run(299)