first_integer = int(input('Enter an integer: '))
second_integer = int(input('Enter an integer: '))
third_integer = int(input('Enter an integer: '))

sum_number = first_integer + second_integer + third_integer
average = sum_number / 3
product = first_integer * second_integer * third_integer

print('Total = ', sum_number)
print('Average = ', average)
print('Product = ', product)

largest = first_integer
if second_integer > largest:
    largest = second_integer
if third_integer > largest:
    largest = third_integer
smallest = first_integer
if second_integer < smallest:
    smallest = second_integer
if third_integer < smallest:
    smallest = third_integer
    
print('Largest is ', largest)
print('Smallest is ', smallest)

