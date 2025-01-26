# Module: A file with some python code
# We use modules to divide our code into multiple files just like sections in a supermarket
# Each of these files is referred to as a module.
#This ensures codes are well-structured, easy to read and re-usable.

import converters                    #imports the program converters
print(converters.kg_to_lbs(70))

#Altenatively. After line6 (import converters), we can do the following:
from converters import kg_to_lbs
print(kg_to_lbs(100))

#Select whatever case works best for you.