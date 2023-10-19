value = float(input("Enter temperature: "))
unit = input("Select unit of measurement (C > F, F > C): ")

if unit == "C":
    fahrenheit = (value * 9/5) + 32
    print(f"{fahrenheit}")
elif unit == "F":
    celsius = (value - 32) * 5/9
    print(f"{celsius:.2f}")
else:
    print("Unsupported unit of measure. Use 'C' for Celsius or 'F' for Fahrenheit.")