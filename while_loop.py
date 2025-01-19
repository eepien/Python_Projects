i = 1                                     #index
while i <= 10:
    print(i)                              # prints i
    print("*" * i)                        # produces a string with i # of asterisks
    i+=1                                  # same as i=i+1 or i=++
print("done")

#===================================
# Guessing game: guesses a secret number max 3 times.
#===================================

guess_count = 1
guess_limit = 3
secret_number = int(input("Enter a secrete Integer:"))

while  guess_count <= guess_limit:
    guess = int(input("Guess an integer: "))
    guess_count+=1
    if guess == secret_number:
        print("You win!")
        break
    else:
        print("You guess wong. Try again")
print("Hope you had fun!")  #Testing the guess game. 01/18

