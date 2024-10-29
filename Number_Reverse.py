#Number Reverser: Write a Python program that takes an integer input from the user and prints its reverse using a while loop.

number=int(input("Enter the digit: "))
reverse_Digit=""
while number>0:
    last_num = number%10
    number = number//10
    print("Last Digit: ",last_num,"Number: ",number)
    reverse_Digit= reverse_Digit+str(last_num)

print("Reverse Number: ",reverse_Digit)

