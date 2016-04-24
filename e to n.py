import math
from decimal import Decimal
from decimal import getcontext

n = input('Enter how many decimal points of e you want to view: ')

max = 100
e = Decimal(1)
getcontext().prec = 40
def fact(p):
    silnia =1
    for i in range(1, int(p)+1):
        silnia *= i
    return (int(silnia))

for k in range(1, max):
    e += Decimal(1/(fact(k)))

print (round(e ,int(n)))

##silnia
