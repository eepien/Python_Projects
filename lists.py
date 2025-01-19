names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)                                          # returns ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0])                                       # returns John
print(names[-1])                               # returns Mary
print(names[2:])                               # returns ['Mosh', 'Sarah', 'Mary']
print(names[2:4])                              # returns ['Mosh', 'Sarah']
names[0] = "Jon"                               # Updates the first list item John to Jon
print(names)                                   # Prints the updated list ['Jon', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(len(names))