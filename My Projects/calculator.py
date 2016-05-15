from math import sqrt
dec = 0
while dec != 'e':
    oper = input("Choose type of operation to perform: a - addition, s - subtraction, m - multiplication, d - division,"
                 "r - root square, p - square power ")
    if oper == 'a':
        a = float(input())
        b = float(input())
        print(a+b)
    if oper == 's':
        a = float(input())
        b = float(input())
        print(a-b)
    if oper == 'm':
        a = float(input())
        b = float(input())
        print(a*b)
    if oper == 'd':
        a = float(input())
        b = float(input())
        print(a/b)
    if oper == 'p':
        a = float(input())
        print(a*a)
    if oper == 'r':
        a = float(input())
        print(sqrt(a))
    dec = input("If you want to exit calculator press 'e', otherwise press any other key ")