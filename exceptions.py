# This code teaches us how to use exceptions to avoid program crashes.
try:
    age = int(input("Enter your age: "))
    income = int(input("Enter your income: "))
    risk = income/age
    print(f" You are {age} years old.")
    print(f"Your risk score is {risk}")

except ValueError:                           #Error that shows up on terminal if this particular error is made.
    print("Invalid age value entered")       #Prints Invalid Value instead of Value Error, for invalid inputs, eg. Age = abc

except ZeroDivisionError:                 #Prevents program from crashing for age = 0 yrs
    print("Age should not be zero")       # returns this error when you enter age = 0 yrs.

# Here is the syntax:
#except <terminal error id>:                  #There can be more than one exceptions
#    print(whatever you want here)