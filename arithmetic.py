print(10+3)
print(10/3)                 #returns float
print(10//3)                #returns integer
print(10%3)                 #returns modulus
print(10*3)                 #multiplication
print(10**3)                #10^3

x = 10
x = x +3

print(x)

y=12
y+=3                      #aumented assignment operator, same as y=y+3
z=15
z-=4                      #agumented assignment operator, same as z=z-4
print(y)
print(z)

t=10+3*2**2               # means t = 10 + 3 * 2^2. Squared will be performed first, then * and finally + BODMAS
print(t)

a= - 2.9
print(round(a))        #rounds float a= -2.9 to the nearest integer
print(abs(a))          #returns the absolute number
import math
print(math.ceil(abs(a)))
print(math.floor(abs(a)))