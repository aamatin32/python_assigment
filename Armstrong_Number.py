#Write a Python program that takes an integer input from the user and checks if it is an Armstrong
# number (a number that is equal to the sum of its own digits raised to the power of the number of digits) using a for loop.

number=int(input("Enter the digit: "))
temp_number=number
sum=0
while number>0:
    last_num = number%10
    number = number//10
    print("Last Digit: ",last_num,"Number: ",number)
    sum+= last_num**3

if sum==temp_number:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")