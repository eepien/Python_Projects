numbers = [3,6,2,8,10,20,15,8]
numbers_copy = numbers.copy()      #makes a copy of our original list
numbers.append(25)               #Adds 25 to the list
print(numbers)                   #Returns the following list [3, 6, 2, 8, 10, 20, 15, 8, 25]
numbers.insert(0,1) # Inserts 1 at index 0 giving new list: [1, 3, 6, 2, 8, 10, 20, 15, 8, 25]
print(numbers)
numbers.pop(4,)        # removes object (in this case 8) from index 4. numbers.pop() will remove last digit on the list
print(numbers)

#Segment below returns the max and min in a list
max = numbers[0]
min = numbers[0]
for number in numbers:
    if number > max:
        max = number
    if number < min:
        min = number
print(f'Min{numbers} = {min} and Max{numbers} = {max}')   #returns min and max number in a list

print(numbers.index(8))                  #Returns index with first appearance of 8. Pgm errors out if # doesn't exist
print(8 in numbers)          #Returns True if number exists in the list.
print(50 in numbers)       #Returns False if number does not exist.
print(numbers.count(20))   #Counts the number of times 20 occurs in this list

print(numbers)
print(numbers.sort())      #Returns an empty list None although our list has been sorted
#Best way to sort a list is to
numbers.sort()             #first sorts the list
print(numbers)             #then print the sorted list in ascending order: [1, 2, 3, 6, 8, 10, 15, 20, 25]

numbers.reverse()          #reverse the sorted list in descending order: [25, 20, 15, 10, 8, 6, 3, 2, 1]
print(numbers)

#Segment below removes all elements in the list
numbers.clear()                    # Removes all elements in the list
print(f"Remaining elements in the cleared list are {numbers}")
print(f"Copy of our original list is {numbers_copy}")