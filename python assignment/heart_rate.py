user_age = int(input('Enter your age: '))

bmp = 220

maximum_heart_rate = bmp - user_age
target_low_heart_rate = maximum_heart_rate * 0.50
target_high_heart_rate = maximum_heart_rate * 0.85

print(maximum_heart_rate)
print('Maximum Heart Rate is: ', maximum_heart_rate, 'bmp')
print('Target Low Heart Rate', target_low_heart_rate, 'bmp')
print('Target High Heart Rate', target_high_heart_rate, 'bmp')
