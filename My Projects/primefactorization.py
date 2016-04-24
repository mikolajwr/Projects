x = input('Podaj liczbe do rozlozenia na czynniki pierwsze: ')
x = int(x)
for i in range(2, x+1):
    while x % i == 0:
        print (i)
        x = x/i