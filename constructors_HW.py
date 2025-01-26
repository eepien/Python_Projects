# Define a new type called person with name attribute and talk method and:
# That is
#     Person
#        -names
#        -talk()

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("talk")

man = Person("John Smith")
print(man.name)
man.talk()
