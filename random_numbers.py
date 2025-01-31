import random

for i in range(5):   #range tells us the number of times we want to iterate the for loop
    print(random.random())  #prints a random # between 0 - 1 for each loop.
    print(random.randint(10,20)) #generates a random number between 10 - 20 for each loop

#===============================
members = ['John', 'Mary', 'Bob', 'Mosh', 'Dylan', 'Rene', 'William', 'Emeh', 'Ian', 'Grace', 'Emma']
leader = random.choice(members)                     #randomly picks an item from the members list
print(leader)