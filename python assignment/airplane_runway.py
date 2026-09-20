airplane_acceleration = float(input('Enter the acceleration rate: '))
airplane_takeoff_speed = float(input('Enter the speed rate: '))

length = (airplane_takeoff_speed ** 2) / (2 * airplane_acceleration)

print('The minimum runway length for this airplane is ', '$',length)
