x = input('Wybierz czy chcesz 1 - podac liczbe do ktorej ma wypisac ciag Fibonacciego '
          '2 - wypisace do n-tej wartosci ciagu Fibonacciego: ')
"""
while x != 1 or x != 2:
    x = input('Komenda nierozpoznana, prosze wpisac jeszcze raz: ')
"""
k=0
y=1
fib=0

if x == '2':
    usrinput = input('Podaj do ktorego n wyrazu ciagu mam wypisac: ')
    if usrinput == '0':
        print (0)
    elif usrinput == '1':
        print (0)
        print (1)
    else:
        print (0)
        print (1)
        for i in range(2, int(usrinput)+1):
            fib = y+k
            k=y
            y=fib
            print (y)
else:
    usrinput = input('Podaj do jakiej liczby mam wypisac ciag: ')
    if usrinput=='0':
        print (0)
    elif usrinput=='1':
        print (0)
        print (1)
        print (1)

    else:
        print (0)
        print (1)
        while y<int(usrinput):
            fib = y+k
            k=y
            y=fib
            if y<=int(usrinput):
                print (y)

