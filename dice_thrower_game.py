# Program throws two dice at once, or one dice twice and returns the output
import random
class Dice:
    def roll(self):
        return random.randint(1,6)


first = Dice().roll()
second = Dice().roll()
print(f'({first}, {second})')

#print(f'({random.randint(1,6)}, {random.randint(1,6)})') #Note that lines 1 and 11 only will do the job