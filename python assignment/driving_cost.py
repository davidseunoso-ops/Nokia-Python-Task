distance = float(input('Enter the driving distance: '))
miles = float(input('Enter miles the per gallon: '))
price = float(input('Enter the price per gallon: '))

cost = distance / miles * price

print('The cost of driving is ', '$',cost)
