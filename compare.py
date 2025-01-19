t=input("Enter today's temperature in C: ")
t = int(t)
if t >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

print()

#================================
#Program validates name length
#================================
name=input("Enter your name: ")

print(f"Hi {name}!")
if len(name) < 3:
    print("Your name must be minimum 3 character.")
elif len(name)> 50:
    print("Your name must be max 50 characters")
else:
    print("Your name looks good!")
print()

#=================================
#Program Weight calculator
#==============================

weight = int(input("Enter your weight: "))                   #Passes weight as an integer
units = input("Is your weight in (K)g or (L)bs: ")

if units.upper() == "K":                                       # converts units to uppercase letter before comparison
    weight_lb = round(weight / 0.45, 2)              #round will round( , 2) the calculated weight to 2 dp
    print("Your weight is ", weight_lb, "lbs" )      #Without using a formated string
elif units.upper() == "L":
    weight_kg = round(weight * 0.45, 2)
    print(f"Your weight is {weight_kg} Kg")          #Using a formated string does the same as line 32
else:
    print("You did not specify the correct units.")
    print("Try again next time.")
print(f"Thank you {name}!")
