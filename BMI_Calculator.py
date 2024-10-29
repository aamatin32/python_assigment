##BMI Calculator: Write a Python program that takes a person's height (in meters)
#and weight (in kilograms) as input and calculates their Body Mass Index (BMI).
#Print out their BMI and a message indicating whether they are underweight
#(<18.5), normal (18.5-24.9), overweight (25-29.9), or obese (>=30).

height = float(input("Enter your height (in meters): "));
weight = float(input("Enter your weight (in kilograms): "));

calculate_BMI = weight/(height*height);
print("BMI value: ",round(calculate_BMI,1))

if calculate_BMI < 18.5:
    BMI_result='Under Weight'
elif calculate_BMI>=18.5 and calculate_BMI<25:
    BMI_result="Normal"
elif calculate_BMI >= 25 and calculate_BMI <30:
    BMI_result='Over Weight'
else:
    BMI_result='Obese'

print("Your Height: ",height," and weight: ",weight,". Your BMI: ",BMI_result)