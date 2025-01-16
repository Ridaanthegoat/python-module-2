#Write a program to create two classes Dog and Cat, with the same attributes - (name and age) and methods - (info and make_sound). 
#Create different objects for each class and pass the parameters. Showcase the concept of polymorphism in this program.

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("I am a cat. My name and age are ",self.name,self.age)
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("I am a dog. My name and age are ",self.name,self.age)
obj1=Cat("ridaan",7)
obj2=Dog("advik",9)
for i in obj1,obj2:
  i.details()
        
