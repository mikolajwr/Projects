def isPrime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True
def genPrime(currentPrime):
    newPrime = currentPrime+1
    while True:
        if not isPrime(newPrime):
            newPrime += 1
        else:
            break
    return newPrime

x = input('Do you want to see first prime number? y/n: ')

if x == 'y':
    print (2)
    currentprime = 2
    while True: #loop to keep asking us if he wants to see the prime number
        x = input('Do you want to see the next prime number? y/n')
        if x == 'y':
            print (currentprime)
            currentprime = genPrime(currentprime)
        else:
            break

else:
    pass