##FizzBuzz: Write a Python program that prints the numbers from 1 to 100. But for
##multiples of three, print "Fizz" instead of the number, and for the multiples of five,
##print "Buzz". For numbers that are multiples of both three and five, print
##"FizzBuzz" using a for loop.

for x in range(1, 101):
  if (x%3== 0 and x%5== 0):
      print("FizzBuzz")
  elif x%3== 0:
      print("Fizz")
  elif x%5==0:
      print("Buzz")
  else:
    print(x)

