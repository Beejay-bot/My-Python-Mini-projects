name = input("What is your name?")
age=int(input("Please enter your age:"))
current_year = 2021
if(current_year%4==0 and current_year%100!=0 or current_year%400==0):
   comment= f"hello {name} you are {age},you were born in {current_year - int(age)}. Your birth year is a leap year"
else:
    comment= f"hello {name} you are {age},you were born in {current_year - int(age)} The year isn't a leap year!"

print(comment)


