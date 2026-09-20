collect_number = int(input('Enter the five digits: '))

digit_one = collect_number // 10000
digit_two = collect_number // 1000 % 10
digit_three = collect_number // 100 % 10
digit_four = collect_number // 10 % 10
digit_five = collect_number % 10

print(digit_one, digit_two, digit_three, digit_four, digit_five)
