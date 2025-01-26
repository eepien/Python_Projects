# This code teaches us how to use exceptions to avoid program crashes.
try:
    age = int(input("Enter your age: "))
    print(f" You are {age} years old.")

except ValueError:                           #Error that shows up on terminal if this particular error is made.
    print("Invalid age value entered")       #Prints Invalid Value instead of Value Error, for invalid inputs, eg. Age = abc

# Here is the syntax:
#except <terminal error id>:                  #There can be more than one exceptions
#    print(whatever you want here)