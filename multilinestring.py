multi_string = """ 
Hi John. 
This is a multiline String. 
Hope you enjoyed it. 
"""

course = 'Python for Beginners'
another = course[:]                          #clone of course
print(multi_string)                          #Returns multi_string above
print(course[0])                             #Returns first letter in the course string, P
print(course[-1])                            #Returns letter of the course string, s
print(course[0:4])                           # Returns the first 4 characters in the course string, Pyth
print(course[0:])                            # Returns everything in the course string, Python for Beginners
print(course[1:])                            # Returns everything but the first character, p. Results: ython for Beginners
print(course[:])                             # python assumes zero as the start index & length of string as end index
print('below is a clone of course: ')
print(another)