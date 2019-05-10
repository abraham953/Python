class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        #print("talking")
        print("Hey I am {}".format(self.name))
    def write(self):
        print("Hey I am {} and I want to write something".format(self.name))

name = input("What is your name? ")
job  = input("What do you want to do? ")
personobjt = Person(name)
if job.lower() == "write":
    personobjt.write()
elif job.lower() == "talk":
    personobjt.talk()
else:
    print("not a correct input")