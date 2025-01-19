#Generates (x,y) coordinates
print("(x, y)")
for x in range(4):                          # outer loop
    for y in range(3):                      # nested for loop, aka inner loop
        print(f"({x}, {y})")                #results (0, 0), (0,1), (0,2), (1, 0), (1, 1), (1, 2),...

#===================================
# Program to create an F on a screen
#===================================

numbers = [5, 2, 5, 2,2]
for i in numbers:
    print("X" * i)                          # Beauty of Python.
print()                                     # Just to create space

#Alternatively

numbs = [5, 2, 5, 2, 2]                     # To output L, you may use the list [2,2, 2, 2, 5]
for x_count in numbs:                       #x_count will take numbers 5, 2, 5, 2, 2
    output = ""
    for count in range(x_count):
        output += "X"
    print(output)