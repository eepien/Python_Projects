# Define a new type called person with name attribute and talk method and:
# That is
#     Person
#        -names
#        -talk()
#Include additional modifications to the program.

class Person:
    def __init__(self, name): #This is the constructor
        self.name = name
    def talk(self):
        print(f" Hi, I am {self.name}")

man1 = Person("John Smith")   # Object man1 is a different instance of Class Person.
man1.talk()

man2 = Person("Bob Dylan")
man2.talk()

#Each object (man1, man2) is a different instant of a Person Class.