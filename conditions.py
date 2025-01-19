is_hot = False
is_cold = False
if is_hot:
    print("It's a  hot day")
    print("Drink Plenty of water")

elif    is_cold:
    print("Its a cold day")
    print("Dress warm")
else:
    print("It's a lovely day")
print("Enjoy your day!")
print()

#===============================================
#Short program for a buyer with good credit
#===============================================
price = 10**6
good_credit =False
#credit = input("Enter your credit scores: ")

if good_credit:
    print("Down payment is: $", price*0.1)
else:
    print("Down payment is: $", price*0.2)
print("Thanks for your business!")
print()
#============================================
#Program Bank Loan
#============================================
high_income = True
good_credit = True
criminal_record = True

if high_income and good_credit and not criminal_record:               #or can be replaced with and
    print("Eligible for Loan")
else:
    print("Not eligible for loan")
print("Thanks for your business!")