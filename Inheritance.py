class Mammal:
    def walk(self):
        print("walk")


class Human(Mammal):
    def talk(self):
        print("talk")

class Dog(Mammal):
    def bark(self):
        print("bark")
Human1 = Human()
Human1.walk()
Dog1 = Dog()
Dog1.bark()
