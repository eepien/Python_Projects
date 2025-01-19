first = "John"
last = 'Smith'
course = 'python for beginners'
message = first + ' [' + last + '] is a coder'
print(message)

#formated string approach below

msg = f'{first} [{last}] is a coder'           #uses {} to dynamically insert variables in your string.
print(msg)

#length of characters on a string using built in function, len

print(len(first))                          #returns the number 4

#Prints string letters to uppercase. upper in this case is a method, not a function. specific to a string.
uc=first.upper()
print(uc)                                    #Prints first name in upper case
print(first)                                 #first name is still in original form
print(first.lower())                         #prints first name in lower case
print(first.find('o'))                       #returns the index position of O in John, which is 1, it is case sensitive
print(last.replace('Smith','Smith Jr.' ))  # Replaces Smith with Smith Jr
print('J' in first)                                   #boolean. Returns True if J is found and False otherwise. Case sensitive
print(course.title())                             #returns Python For Beginners.