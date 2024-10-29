#Temperature Converter: Write a Python program that takes a temperature input
#in Celsius and converts it to Fahrenheit if the temperature is above 0°C, or to
#Kelvin if the temperature is below 0°C.


temperature_in_celsius = float(input("Enter temperature (in celsius): "));

convert_temperature = (temperature_in_celsius*9 /5) + 32

print("Temperature in Celsius: ",temperature_in_celsius," in  Fahrenheit: ",convert_temperature)
