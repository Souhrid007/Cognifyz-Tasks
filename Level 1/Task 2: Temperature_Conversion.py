def celsi_to_fahren(celsius):
    return (celsius * 9/5) + 32

def fahren_to_celsi(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()

    if unit == "C":
        converted_temp = celsi_to_fahren(temp)
        print(temp, "°C is", converted_temp, "°F")
    elif unit == "F":
        converted_temp = fahren_to_celsi(temp)
        print(temp, "°F is", converted_temp, "°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

convert_temperature()
