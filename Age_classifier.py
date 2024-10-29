#Age Classifier: Write a Python program that takes a person's age as input and
#prints out whether they are an infant (0-1), toddler (1-3), child (4-12), teenager
#(13-19), adult (20+).

age =int(input("Enter your age: "))

if age>=0 and age<1:
    age_classsifier = 'Infant'
elif age>=1 and age<=3:
    age_classsifier = 'Toddler'
elif age>=4 and age<=12:
    age_classsifier = 'Child'
elif age>=13 and age<=19:
    age_classsifier = 'Teenager'
else:
    age_classsifier = 'Adult'

print("You are ",age,"year(s) old and you are in: ", age_classsifier, "age group")