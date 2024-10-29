###Problem: Largest among Three Numbers: Write a Python program that takes three
# numbers as input and prints out the largest among them.


number_1, number_2, number_3 = input("Enter three numbers: ").split()

if number_1>=number_2 and number_1>=number_3:
    largest_number= number_1
elif number_2>=number_1 and number_2>=number_3:
    largest_number = number_2
else:
    largest_number = number_3

print("Among ",number_1, ",", number_2, "," ,number_3, "Largest No: ",largest_number)
