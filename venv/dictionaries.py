#What was traditionally called records
customer = {
    "name": "John Smith",
    "age": 30,
     "is verified": True
}

print(customer["name"])             #Returns John Smith. Program errors out if customer argument is not found
print(customer.get("name"))         #Equally returns Name. Is preferable because it returns none if argument is absent
print(customer.get("birthdate"))    #Returns None.
print(customer.get("birthdate", "Jan 1 1980"))  #supplies default value of Jan 1 1980.

customer["name"] = "Jack Smith"      #updates customer name to Jack Smith.
print(customer["name"])

customer["birthplace"] = "Oregon"
print(customer["birthplace"])        #add birthplace to the dictionary
print()
#================================================
# Program maps phone numbers from digits to word
#================================================
phone = input("Enter Your Phone Number: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, '!') + " "     # the last " " provides space between the words
print(output)
print()
