cost = input("How much does the product cost:")
amount_paid = input("How much money client gave:") #penny - 1 cent, dime-10cent, nickel-5centów
cost = float(cost)
amount_paid = float(amount_paid)
while amount_paid<cost:
    amount_paid = input("You didn't pay enough ")
    amount_paid = float(amount_paid)
change = amount_paid - cost
print("The change is equal to ", round(change,2))
cents = round(change,2)*100
quarter = 0
dime = 0
nickel = 0
penny = 0
while cents>0:
    if cents>=25:
        quarter += 1
        cents -= 25
    elif cents>=10:
        dime += 1
        cents -= 10
    elif cents>=5:
        nickel += 1
        cents -= 5
    else:
        penny += 1
        cents -= 1
print("Change consists of %s quarters, %s dimes, %s nickels and %s pennys" % (quarter, dime, nickel, penny))