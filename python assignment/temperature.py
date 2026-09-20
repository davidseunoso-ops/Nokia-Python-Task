celsius = float(input("Enter a temperature in celsius: "))

for count in range(5):
    temperature = celsius + count
    
    if temperature < -273:
        print("impossible!")
        a
    else:
        fahrenheit = (temperature * (9/5) + 32)
        print(fahrenheit)
