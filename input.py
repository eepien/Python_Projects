name = input("What is your name? ")
birth_year = input("Enter your Birth Year: ")              #birthyear is a string here, not a number
color = input("what is your favorite color? ")
age = 2024 - int(birth_year)                               #Inte passes variable birth_year into an integer
weight_lb = input("Enter your weight in Lbs: ")
weight_kg = 0.453 * float(weight_lb)                       #converts weight_lb from string to float
print('Hi ' + name)                                        # + concatenates Hi and your name. For example. Hi Nzumbe
print(name + ' is ',  age , ' years old.')
print(name + ' likes ' + color)
print(name + ' is ', round(weight_kg, 3), ' Kg')          #Rounds weight in kg to 3 decimal places.
