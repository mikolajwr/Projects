from math import ceil
x = input('What is width of the floor: ')
y = input('What is length of the floor: ')
cost = input('What is a cost of tile: ')
tileX = input('What is tile width: ')
tileY = input('What is tile length: ')
x = float(x)
y = float(y)
tileY = float(tileY)
tileX = float(tileX)
cost = float(cost)
sumTiles = x*y/(tileX*tileY) #amount of tiles required to cover whole floor
print ('You need %s tiles to cover whole floor' % ceil(sumTiles))
print ('The cost of tiles is: ', ceil(sumTiles)*cost )