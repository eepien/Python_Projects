for item in 'Python':                                       #List of characters can be put in single quotes
    print(item)

for names in ['Emeh', 'William', 'Grace', 'Ian', 'Epie']:   #use curly braces for a list of items
    print(names)

for numbers in [1, 2, 3, 4, 5]:               #print numbers from 1-5 range, one per line
    print(numbers)

for numbers in range(6):                       #print numbers in range 1-5. Note that it excludes 6
    print(numbers)

for numbers in range(5, 10):                    #prints numbers in range 5 - 9.
    print(numbers)

for numbers in range(5, 10, 2):                 #prints numbers in range 5-9 in steps of 2. i.e. 5, 7, 9
    print(numbers)

#================================================
#Calculates cost of all items in a shopping cart
#=================================================
prices = [10, 20, 30]
total_cost = 0
for price in prices:
    total_cost += price                            # can also be written total_cost = total_cost + price
print(f"Total cost = $ {total_cost}.00")           #Note we used formated string here.