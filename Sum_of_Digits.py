#Sum of Digits: Write a Python program that takes an integer input from the user and calculates the sum of its digits using a while loop.

number=int(input("Enter the digit: "))
sum=0
while number>0:
    last_num = number%10
    number = number//10
    print("Last Digit: ",last_num,"Number: ",number)
    sum+= last_num

print("Digit's Sum:  ",sum)