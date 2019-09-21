class Dog:
    def eat(self, food):
        print(self.color, '的', self.kinds, '正在吃', food)

dog1 = Dog()
dog1.kinds = '京巴'
dog1.color = '白色'
dog1.color = '黄色' # this line will overwrite the color-attribute of dog1
dog1.eat('骨头')

dog2 = Dog()
dog2.kinds = '牧羊犬'
dog2.color = '灰色'
dog2.eat('屎')