numbers =[1, 2, 2, 4, 3, 5, 2, 5, 4, 10, 15]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
