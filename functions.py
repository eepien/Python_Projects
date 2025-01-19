from emoji_converter import output


def greet_user():                            #Defines the function
    print("Hi there!")
    print("Welcome aboard")
                                            #Always good practice to skip 2 line after the function

print("Start")
greet_user()
print("Finish")
print()
#==================================
# Function that passes a parameter
#===================================
def greet_user2(name):       #name is a global parameter (place holder)
    print(f"Hi {name}")
    print("Welcome aboard")

print("Start")
greet_user2("John")      #If we miss adding the parameter, program crashes.
greet_user2("Mary")      # John and Mary are arguments (actual values)
print("Finish")

#=====================================
#Function returns first and last name
#=======================================
def greet_user3(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

print("Start")
greet_user3("John", "Smith")
greet_user3("Mary", "Parker")
print("Finish")

#=============================
# Return function
#=============================
def square(number):
    return number * number                  #return prevents function from returning None (default)

print(square(3))

#==============================
# Function Emoji converter
#============================
def emoji_conv(message):
    words = message.split(" ")
    # print(words)
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")
results = emoji_conv(message)
print(results)

