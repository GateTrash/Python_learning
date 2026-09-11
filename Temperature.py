temp_system = int(input("Change a temperature system: (1-Celsium; 2-Fahrenheit) "))
temperature = float(input("Enter the temperature "))
if temp_system == 1:
    print(f"{temperature} °C =={temperature * 9 / 5 + 32}°F")
elif temp_system == 2:
    print(f"{temperature} °F = {(temperature - 32) * 5 / 9}°C")
else:
    print("unknown metric system")