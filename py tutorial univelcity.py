# mynumber =20.234
# rounded_num = round(mynumber, 2)
# print(rounded_num)

# num =22
# den =7
# pi = num/den
# print(pi)
# round_pi = round(pi,3)
# print(round_pi)

# name = "Elson"
# surname = "john"
# fullname = name + " "+ surname
# print(fullname)

# day = "20"
# month = "may"
# year = "2019"
# print(day + "/" + month + "/" + year)

# pi = 22/7
# print (pi)
# statement = "pi is  " + str(round(pi,2)) 
# print (statement) 

# akara_price = 20
# akamu_price = 50
# akara = input('please how many akara do you want? :') 
# akamu = input ('how many akamu do you want ? :')
# print (akara, akamu)

# akara_statement = "you bought"  + akara + " " + "akara" 
# akamu_statement = "you bought" + akamu + " "+  "akamu"
# print(akara_statement)
# print(akamu_statement)
# bill = "your bill is :" + str(akara_price * int(akara) + akamu_price * int(akamu) )
# print(bill)  

# name = input("Please your name?")
# age = input("please your age?")
 
# comment= f"hello {name} you are {age},you were born in {2019 - int(age)}"
# print(comment)

# name = input("Please your name? ")
# print(name[1], name[3], name[5])
# print(name[-1])
# print(name[0:5])

# word = input("type in a word :")
# length_of_word = input("please input number of characters :")

# split = int(int(length_of_word)/2) - 1
# two_chars_up = split + 2
# first_two = word[0:2]
# last_two = word[-2:]
# mid_point = word [split : two_chars_up]
# statement = f"{first_two}{mid_point}{last_two}"
# print(statement)
# # print(word[split:two_chars_up])

# word = "sweet mum"
# slice = word[:-4]
# print(slice)

# a = int(input("what is your a?"))
# b = int(input("what is your b?"))
# c = int(input("what is your c?"))
# num = ( (int(b)**2 ) - (4 * int(a*c) )  )** 0.5
# den = (2 * a)
# x1 = ((-b+num)/den)
# x2 = ((-b-num)/den)
# y = ((a**2)+(b**2))**0.5

# print(x1, x2)

# age = int(input('please enter your age :')) 

# can_drink = age >= 20
# can_pay_tax = age >= 18
# can_take_pension = age > 60
# can_retire = age == 40 

# statement = f"can drink : {can_drink}\n can pay tax : {can_pay_tax}\nCan take pension : {can_take_pension}\nCan now retire : {can_retire} "
# print(statement)

# file = open("my data.csv", 'w')
# # print(1,2,3,4, file = file, sep = ",")
# file= open("my_data.csv," 'a')
# print("name", "Age","state","Due", file= file,sep = ",")
# print("ade", 20, "osunstate", 20000, file= file,sep = ",")
# file = open('my_data.csv', 'w')
# details = input ('enter your details in this format name,age,state, dues:')
# splitted_details = details.split (",")
# print (splitted_details[0], splitted_details[1], splitted_details[3], file = file,sep = ",")


                        #  COMMON STRING OPRATIONS
# my_range = range(20, 60, 2)
# print(my_range)
# print(type(my_range))
# print(list(my_range))
# print(list(reversed(my_range)))

# x = [1,2,5,3,10,1,0,4]
# print(sorted(x, reverse = True))

# x= set("abimbola")
# print(set(x))

# my_list = ["seed", "bee", "a", 'cheeked', 'print']
# print(sorted(my_list, key = len, reverse= True))

# my_dict = dict(a=20, b=30)
# print(my_dict)
# print(my_dict['a'])

# nums = [1,2,3,4,5]
# mapped = map (lambda x : x*2, nums)
# print(list(mapped))

# names = ['ade', 'john', 'shola',]
# mapped = map(lambda x : " mr " + x, names)
# print(list(mapped))

# word = input ("please input a word") .lower()

# response = 'a' in word or 'e' in word or 'i' in word or 'u' in word
# print(f' contains vowels : {response}')

# word = input("please input a word thats start with 'PRE' : ")
# replace_word = word.replace("pre", "post")
# print(replace_word)

# text = ['gem', 'hem', 'blem', 'chem']
# mapped = map(lambda x : x.replace('e', "a"), text)
# print(list(mapped))

# data = [ 1, 3, 1, 2, 2, 4]
# mean = sum(data)/len(data)
# mapped = list(map(lambda a : (a-mean)**2, data))
# print((mapped))
# sum_of_squares = sum(mapped)
# n_1 = (len (data))
# print(n_1)
# print(sum_of_squares/(len(data)-1))

# a = ['hello', 'world']
# name = ' '.join(a)
# print(name)

# 
                 #    ASSIGNMENT 1
# import random 
# for x in range(2):
#    print(random.randint(1,6))
# if random.randint is (6,6) is True:
#     print("you win")
# else:
#     print("try again")

#                 #   ASSIGNMENT 2
# three_friends = ["bola", "chisom", "james"]
# no_of_friends = (len(three_friends))
# candies = int(input("number of candies:"))
# a =int(candies/no_of_friends)
# remainder = int(candies % 3)
# statement = f' number of candy to be shared is : {a}\n number of candies to be crushed : {remainder}'
# print(statement)

#             # assignment 3
# name = [(' ' 'Ade', 'm'), ([' ''shade', 'f']), ([' ' 'john', 'm']), ([' ' 'bolu', 'f'])]
# raw_saluted_name = map(lambda x : "Mr" +  x[0] if x[1] == "m" else "Mrs" + x[0], name)
# saluted_name = list(raw_saluted_name)
# print(saluted_name)

#  x = 0
#  y = 5
# if x or y:
#     print('yes')

# if 'foo' in ['foo', 'bar', 'baz']:
#     print('Outer condition is true')      

#     if 10 > 20:                           
#         print('Inner condition 1')        

#     print('Between inner conditions')    

#     if 10 < 20:                           
#         print('Inner condition 2')        

#     print('End of outer condition')       
# print('After outer condition')

# behaviour = input('input either good or bad:')
# age =int(input('enter your age:'))

# if behaviour == "good" and age < 18:
#     print('you get a car')
# if behaviour == "good" and age > 18:
#     print('you get a car')
# if behaviour == "bad":
#     print('GET OUT!!!!')


# score = int(input("what is your score?"))
# f = 'fail' if score< 50 else 'pass'
# print(f)

# health_status = str(input('answer with yes or no : ARE YOU OKAY?'))
# print(health_status)
# if health_status == 'yes':
#     print('Please get a life')
# else:
#     question_2= str(input('Do you have pains?'))
#     print(question_2)
#     if question_2== "no":
#         print('unable to diagnose')
    
#     else:
#         question = str(input('Did you sleep well?'))
#         print(question)
#     if question == 'no':
#         print('Try to sleep') 
#     else:
#         hardwork =str(input('have you done any hardwork?'))
#         print(hardwork)
#     if hardwork == 'no':
#         print('have some pain killer')
#     else:
#         fever = str(input('Do you have fever?'))
#         print(fever)
#     if fever == "yes":
#         print("inconclusive see a doctor?")
#     else:
#         vommiting = str(input('Are you vommiting?'))
#         print(vommiting)
#     if vommiting == 'yes':
#         print('see a doctor')
#     else:
#          print("Take some anti-malaria")

# saved_password = input('Please enter password :')
# if saved_password == "bolaji"
#     print('Welcome, correct password')
# else:
#     print('Incorrect password, pleas try again')
qualified_income = 50000
finiancial_status = input("What is your income per-month: ")
if finiancial_status == "50000":
    print('congratulation!!!, You are qualified to take a loan')
if finiancial_status < '50000':
    print('Sorry, you are not qualified to take a loan')
else: 
    print('congrats, you are qualified to borrow loan')

                                #LOOPS
