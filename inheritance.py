# Inheritance is a method for re-using codes.
# Most languages that support classes also support inheritance. It is not typical of python alone.
# Inheritance helps us avoid repetitions in coding. Repetition makes code modification very difficult.

class Mammal:

    def walk(self):
        print("Walks")

    def bark(self):
        print("Barks")

class Dog(Mammal):# the Dog class inherits all attributes of the Mammal class.
    pass          # pass tells python to not expect explicit attributes to the Dog class.


class Cat(Mammal):
   def be_annoying(self):
       print("Annoying")

print("Dog Behaviors:")
dog1 = Dog()
dog1.walk()
dog1.bark()
print("*******************")
print("Cat Behaviors:")
cat1 = Cat()
cat1.be_annoying()
