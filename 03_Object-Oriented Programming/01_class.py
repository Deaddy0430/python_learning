class Dog:  #define a class called 'Dog'
    def eat(self, food):
        print("this dog is eatting", food)

    def sleep(self, hour):
        print("this dog has slept for %d hours" %hour)

dog1 = Dog()    #create a 'Dog' typed object
dog1.eat("shit")

dog2 = Dog()    #create another 'Dog' typed object
dog2.sleep(50)
