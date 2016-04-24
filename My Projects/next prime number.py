x = input('Do you want to see first prime number? y/n: ')
if x == 'y':
    print (2)
    formerprime = 2
    l = 2
    z = 10
    while 1 != 2: #loop to keep asking use if he wants to see the prime number
        y = input('Do you want to see the next prime number? y/n')
        if y == 'y':
            formerprime = l
            z = z+10
            for i in range(formerprime, z+1):
                while z % i == 0:
                    z = z/i
                    l = i
                print (l)

        else:
            break

else:
    pass